import asyncio
import logging
import struct
from asyncio import StreamReader, StreamWriter, Task

import websockets
from websockets.asyncio.client import ClientConnection

logger = logging.getLogger('Connection')


class Connection:
    connected = False
    server_addr = None

    _stream_reader: StreamReader = None
    _reader_loop: Task | None = None

    _stream_writer: StreamWriter = None
    _writer_loop: Task | None = None

    _readbuf = b''
    send_queue = asyncio.Queue()
    recv_queue = asyncio.Queue()

    event_connected = asyncio.Event()

    @property
    def local_address(self):
        return self._stream_writer.get_extra_info('sockname')[0]

    async def connect(self, server_addr):
        raise NotImplementedError

    async def disconnect(self):
        if not self.event_connected.is_set():
            return
        self.event_connected.clear()

        self.server_addr = None

        if self._reader_loop:
            self._reader_loop.cancel()
            self._reader_loop = None

        if self._writer_loop:
            self._writer_loop.cancel()
            self._writer_loop = None

        self._readbuf = b''
        self.send_queue._queue.clear()
        self.recv_queue._queue.clear()
        await self.recv_queue.put(StopIteration)

        if self._stream_writer:
            logger.debug('wait close')
            self._stream_writer.close()
            await self._stream_writer.wait_closed()

        logger.debug('Disconnected.')

    async def __aiter__(self):
        while True:
            result = await self.recv_queue.get()
            if result is StopIteration:
                raise result
            yield result

    async def put_message(self, message):
        await self.send_queue.put(message)

    async def _reader_loop_func(self):
        raise NotImplementedError

    async def _writer_loop_func(self):
        raise NotImplementedError


class TCPConnection(Connection):
    MAGIC = b'VT01'
    FMT = '<I4s'
    FMT_SIZE = struct.calcsize(FMT)

    async def connect(self, server_addr):
        self.server_addr = server_addr
        try:
            # Open a TCP connection
            self._stream_reader, self._stream_writer = await asyncio.open_connection(
                self.server_addr[0], self.server_addr[1]
            )

            logger.debug('Connected.')
            self.event_connected.set()

            # Start reading and writing loops
            self._reader_loop = asyncio.create_task(self._reader_loop_func())
            self._writer_loop = asyncio.create_task(self._writer_loop_func())

            await self.event_connected.wait()
            return True
        except Exception as e:
            logger.error(f'Connection failed: {e}')
            return False

    async def _writer_loop_func(self):
        while True:
            message = await self.send_queue.get()
            packet = struct.pack(TCPConnection.FMT, len(message), TCPConnection.MAGIC) + message
            try:
                self._stream_writer.write(packet)
                await self._stream_writer.drain()
            except Exception:
                logger.debug('Connection error (writer).')
                await self.disconnect()
                return

    async def _reader_loop_func(self):
        while True:
            try:
                data = await self._stream_reader.read(16384)
                if not data:
                    logger.debug('Connection closed or no data received.')
                    await self.disconnect()
                    return

                logger.debug(f'Received data: {data}')
                self._readbuf += data
                await self._read_packets()

            except asyncio.CancelledError:
                logger.debug('Reader loop was cancelled.')
                break
            except Exception as e:
                logger.debug(f'Reader error: {e}')
                await self.disconnect()
                return

    async def _read_packets(self):
        header_size = TCPConnection.FMT_SIZE
        buf = self._readbuf

        while len(buf) >= header_size:
            try:
                message_length, magic = struct.unpack_from(TCPConnection.FMT, buf)

                if magic != TCPConnection.MAGIC:
                    logger.debug(f'Invalid magic, got {repr(magic)}')
                    await self.disconnect()
                    return

                packet_length = header_size + message_length

                if len(buf) < packet_length:
                    return  # not enough data to read the full message

                message = buf[header_size:packet_length]
                buf = buf[packet_length:]  # remove processed data

                await self.recv_queue.put(message)

            except struct.error as e:
                logger.error(f'Error unpacking packet: {e}')
                await self.disconnect()
                return

        self._readbuf = buf


class WebsocketConnection(Connection):
    ws: ClientConnection = None

    def __init__(self):
        super().__init__()
        self.event_wsdisconnected = asyncio.Event()

    @property
    def local_address(self):
        if self.ws is None:
            raise RuntimeError('WebSocket connection not established yet.')
        return self.ws.local_address[0]

    async def connect(self, server_addr: tuple[str, int]):
        host, port = server_addr
        uri = f'wss://{host}:{port}/cmsocket/'

        try:
            # Create websocket connection
            self.ws = await websockets.connect(uri)
            logger.debug('Connected to WebSocket.')

            self.event_connected.set()

            # Start reading and writing loops
            asyncio.create_task(self._reader_loop_func())
            asyncio.create_task(self._writer_loop_func())

            await self.event_connected.wait()
            return True
        except Exception as e:
            logger.error(f'WebSocket connection failed: {e}')
            return False

    async def _writer_loop_func(self):
        while True:
            message = await self.send_queue.get()
            try:
                logger.debug(f'Sending WebSocket message of length {len(message)}')
                await self.ws.send(message)
            except Exception:
                logger.debug('Connection error (writer).')
                await self.disconnect()
                return

    async def _reader_loop_func(self):
        while True:
            try:
                data = await self.ws.recv()
                if data is None:
                    logger.debug('Connection error (reader).')
                    await self.disconnect()
                    return

                logger.debug(f'Received WebSocket message of length {len(data)}')
                await self.recv_queue.put(data)
            except Exception as e:
                logger.debug(f'Reader error: {e}')
                await self.disconnect()
                return

    async def disconnect(self):
        self.event_wsdisconnected.clear()

        if self.ws is not None:
            logger.debug('Disconnecting WebSocket...')
            await self.ws.close()

        await super().disconnect()
