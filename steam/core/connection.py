import asyncio
import logging
import ssl
import struct
from asyncio import Event, Queue

import certifi
import websockets

# import gevent
# from gevent import event, queue, socket
# from gevent.select import select as gselect

logger = logging.getLogger('Connection')


class Connection:
    def __init__(self):
        self.socket = None
        self.connected = False
        self.server_addr = None

        self._reader = None
        self._writer = None
        self._readbuf = b''
        self.send_queue = Queue()
        self.recv_queue = Queue()

        self.event_connected = Event()

    @property
    def local_address(self):
        return self.socket.getsockname()[0]

    async def connect(self, server_addr):
        logger.debug('Attempting connection to %s', str(server_addr))

        try:
            await self._connect(server_addr)
        except OSError:
            return False

        self.server_addr = server_addr
        self.recv_queue.queue.clear()

        self._reader = asyncio.create_task(self._reader_loop)
        self._writer = asyncio.create_task(self._writer_loop)

        # how this gets set is implementation dependent
        await asyncio.wait_for(self.event_connected.wait(), timeout=10)
        return True

    async def disconnect(self):
        if not self.event_connected.is_set():
            return
        self.event_connected.clear()

        self.server_addr = None

        if self._reader:
            self._reader.kill(block=False)
            self._reader = None
        if self._writer:
            self._writer.kill(block=False)
            self._writer = None

        self._readbuf = b''
        self.send_queue.queue.clear()
        self.recv_queue.queue.clear()
        await self.recv_queue.put(StopIteration)

        self.socket.close()

        logger.debug('Disconnected.')

    def __iter__(self):
        return self.recv_queue

    async def put_message(self, message):
        await self.send_queue.put(message)

    async def _connect(self, server_addr):
        raise TypeError('{}: _connect is unimplemented'.format(self.__class__.__name__))

    async def _reader_loop(self):
        raise TypeError('{}: _reader_loop is unimplemented'.format(self.__class__.__name__))

    async def _writer_loop(self):
        raise TypeError('{}: _writer_loop is unimplemented'.format(self.__class__.__name__))


# class TCPConnection(Connection):
#     MAGIC = b'VT01'
#     FMT = '<I4s'
#     FMT_SIZE = struct.calcsize(FMT)
#
#     def _new_socket(self):
#         self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     def _connect(self, server_addr):
#         self.socket.connect(server_addr)
#         logger.debug('Connected.')
#         self.event_connected.set()
#
#     def _read_data(self):
#         try:
#             return self.socket.recv(16384)
#         except OSError:
#             return ''
#
#     def _write_data(self, data):
#         self.socket.sendall(data)
#
#     def _writer_loop(self):
#         while True:
#             message = self.send_queue.get()
#             packet = struct.pack(TCPConnection.FMT, len(message), TCPConnection.MAGIC) + message
#             try:
#                 self._write_data(packet)
#             except:
#                 logger.debug('Connection error (writer).')
#                 self.disconnect()
#                 return
#
#     def _reader_loop(self):
#         while True:
#             rlist, _, _ = gselect([self.socket], [], [])
#
#             if self.socket in rlist:
#                 data = self._read_data()
#
#                 if not data:
#                     logger.debug('Connection error (reader).')
#                     self.disconnect()
#                     return
#
#                 self._readbuf += data
#                 self._read_packets()
#
#     def _read_packets(self):
#         header_size = TCPConnection.FMT_SIZE
#         buf = self._readbuf
#
#         while len(buf) > header_size:
#             message_length, magic = struct.unpack_from(TCPConnection.FMT, buf)
#
#             if magic != TCPConnection.MAGIC:
#                 logger.debug('invalid magic, got %s' % repr(magic))
#                 self.disconnect()
#                 return
#
#             packet_length = header_size + message_length
#
#             if len(buf) < packet_length:
#                 return
#
#             message = buf[header_size:packet_length]
#             buf = buf[packet_length:]
#
#             self.recv_queue.put(message)
#
#         self._readbuf = buf


class TCPConnection(Connection):
    MAGIC = b'VT01'
    FMT = '<I4s'
    FMT_SIZE = struct.calcsize(FMT)

    async def _connect(self, server_addr):
        # 使用 asyncio 的异步连接
        self._reader, self._writer = await asyncio.open_connection(*server_addr)
        logger.debug('Connected.')
        self.event_connected.set()

    async def _read_data(self):
        try:
            data = await self._reader.read(16384)  # 从 _reader 中异步读取数据
            return data
        except asyncio.CancelledError:
            return b''

    async def _write_data(self, data):
        try:
            self._writer.write(data)  # 使用 _writer 发送数据
            await self._writer.drain()  # 确保数据已写入
        except asyncio.CancelledError:
            logger.debug('Connection error (writer).')
            await self.disconnect()

    async def _writer_loop(self):
        while True:
            message = await self.send_queue.get()
            packet = struct.pack(TCPConnection.FMT, len(message), TCPConnection.MAGIC) + message
            try:
                await self._write_data(packet)
            except Exception:
                logger.debug('Connection error (writer).')
                await self.disconnect()
                return

    async def _reader_loop(self):
        while True:
            data = await self._read_data()

            if not data:
                logger.debug('Connection error (reader).')
                await self.disconnect()
                return

            self._readbuf += data
            await self._read_packets()

    async def _read_packets(self):
        header_size = TCPConnection.FMT_SIZE
        buf = self._readbuf

        while len(buf) > header_size:
            message_length, magic = struct.unpack_from(TCPConnection.FMT, buf)

            if magic != TCPConnection.MAGIC:
                logger.debug(f'invalid magic, got {repr(magic)}')
                await self.disconnect()
                return

            packet_length = header_size + message_length

            if len(buf) < packet_length:
                return

            message = buf[header_size:packet_length]
            buf = buf[packet_length:]

            await self.recv_queue.put(message)

        self._readbuf = buf


class WebsocketConnection(Connection):
    def __init__(self):
        super().__init__()
        self.ws = None
        self.ssl_ctx = ssl.create_default_context(cafile=certifi.where())
        self.event_wsdisconnected = Event()

        self._reader_task = None
        self._writer_task = None

    async def connect(self, server_addr):
        host, port = server_addr
        uri = f'wss://{host}:{port}/cmsocket/'

        try:
            # 使用 websockets 库建立异步连接
            self.ws = await websockets.connect(uri, ssl=self.ssl_ctx)
            self.server_addr = server_addr

            # 清理旧的消息队列
            self.recv_queue.queue.clear()

            # 启动接收和发送消息的任务
            self._reader_task = asyncio.create_task(self._reader_loop())
            self._writer_task = asyncio.create_task(self._writer_loop())

            # 等待连接完成
            await asyncio.wait_for(self.event_connected.wait(), timeout=10)
            logger.debug(f'Connected to {uri}')
            return True

        except Exception as e:
            logger.error(f'Failed to connect to {uri}: {e}')
            return False

    async def disconnect(self):
        if not self.event_connected.is_set():
            return

        self.event_connected.clear()
        self.server_addr = None

        if self._reader_task:
            self._reader_task.cancel()
            self._reader_task = None
        if self._writer_task:
            self._writer_task.cancel()
            self._writer_task = None

        self._readbuf = b''
        self.send_queue.queue.clear()
        self.recv_queue.queue.clear()
        await self.recv_queue.put(StopIteration)

        if self.ws:
            await self.ws.close()

        logger.debug('Disconnected.')

    async def put_message(self, message):
        await self.send_queue.put(message)

    async def _reader_loop(self):
        while True:
            try:
                data = await self.ws.recv()
                logger.debug(f'Received {len(data)} bytes')

                if isinstance(data, bytes):
                    await self.recv_queue.put(data)
                elif isinstance(data, str):
                    logger.debug(f'Received message: {data}')
            except Exception as e:
                logger.debug(f'Connection error (reader): {e}')
                await self.disconnect()
                break

    async def _writer_loop(self):
        while True:
            message = await self.send_queue.get()
            try:
                logger.debug(f'Sending message of length {len(message)}')
                await self.ws.send(message)
            except Exception as e:
                logger.debug(f'Connection error (writer): {e}')
                await self.disconnect()
                break


#
# class UDPConnection(Connection):
#     def _new_socket(self):
#         self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
