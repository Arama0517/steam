import asyncio

from pyee.asyncio import AsyncIOEventEmitter


class EventEmitter(AsyncIOEventEmitter):
    def __init__(self):
        super().__init__()
        self._events = {}

    async def wait_event(self, event, timeout=None, raises=False):
        """
        Waits for an event to be emitted, with a timeout and option to raise an exception.
        :param event: The event to wait for.
        :param timeout: The maximum time to wait in seconds.
        :param raises: Whether to raise an exception on timeout.
        :return: The event arguments or None if timeout.
        """
        # 使用 asyncio Event 来等待事件
        event_obj = asyncio.Event()
        self._events[event] = event_obj

        result = None

        def handler(*args):
            nonlocal result
            result = args
            event_obj.set()  # 事件触发，通知等待任务继续

        self.on(event, handler)

        # 等待事件发生或超时
        try:
            await asyncio.wait_for(event_obj.wait(), timeout)
        except asyncio.TimeoutError:
            if raises:
                raise
            result = None

        # 清理事件
        del self._events[event]
        return result
