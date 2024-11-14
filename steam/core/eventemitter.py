import asyncio
from collections import OrderedDict, defaultdict


class EventEmitter:
    """
    Implements event emitter using asyncio.
    Every callback is executed via asyncio.create_task.
    """

    def __init__(self):
        self.__callbacks = defaultdict(OrderedDict)
        self.__queue = asyncio.Queue()
        self.__worker = None

    async def emit(self, event, *args):
        """
        Emit event with some arguments
        """
        await self.__queue.put((event, args))
        await self.__queue.put((None, (event,) + args))

        if self.__worker is None or self.__worker.done():
            self.__worker = asyncio.create_task(self.__emit_worker())

    async def __emit_worker(self):
        while not self.__queue.empty():
            event, args = await self.__queue.get()

            if event in self.__callbacks:
                for callback, once in list(self.__callbacks[event].items()):
                    if once:
                        self.remove_listener(event, callback)

                    if isinstance(callback, asyncio.Future):
                        callback.set_result(args)
                    else:
                        asyncio.create_task(callback(*args))

    def on(self, event, callback=None, once=False):
        """
        Registers a callback for the specified event
        """
        if callback:
            self.__callbacks[event][callback] = once
            return

        # Decorator form
        def wrapper(callback):
            self.__callbacks[event][callback] = once
            return callback

        return wrapper

    def once(self, event, callback=None):
        """
        Register a callback, but call it exactly one time
        """
        return self.on(event, callback, once=True)

    async def wait_event(self, event, timeout=None, raises=False):
        """
        Blocks until an event and returns the results
        """
        future = asyncio.get_event_loop().create_future()
        self.once(event, future)

        try:
            return await asyncio.wait_for(future, timeout)
        except asyncio.TimeoutError:
            self.remove_listener(event, future)

            if raises:
                raise
            else:
                return None

    def remove_listener(self, event, callback):
        """
        Removes callback for the specified event
        """
        if event in self.__callbacks:
            del self.__callbacks[event][callback]

            if not self.__callbacks[event]:
                del self.__callbacks[event]

    def remove_all_listeners(self, event=None):
        """
        Removes all registered callbacks, or all
        registered callbacks for a specific event
        """
        if event is None:
            self.__callbacks.clear()
        elif event in self.__callbacks:
            del self.__callbacks[event]

    def count_listeners(self, event):
        """
        Returns a count of how many listeners are
        registered for a specific event
        """
        return len(self.__callbacks[event]) if event in self.__callbacks else 0
