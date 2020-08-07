import asyncio
import json

import websockets

from .state import ViewState


URL = "wss://osmarks.tk/ewo-ws/"

class Player:
    def __init__(self):
        self.ws = None
        self.loop = asyncio.get_event_loop()

    async def on_state_change(self, new_state: ViewState):
        pass

    async def on_connect(self):
        pass

    def event(self, func):
        if func.__name__.startswith("on_") and hasattr(self, func.__name__):
            setattr(self, func.__name__, func)
        return func

    async def wait_until_ready(self):
        while self.ws is None:
            await asyncio.sleep(0)

    async def move(self, direction: str):
        await self.wait_until_ready()
        await self.ws.send(json.dumps({"input": direction}))

    async def start(self, icon: str):
        async with websockets.connect(URL) as self.ws:
            await self.ws.send(json.dumps({"icon": icon}))
            self.loop.create_task(self.on_connect())
            while not self.ws.closed:
                message = await self.ws.recv()
                self.loop.create_task(self.on_state_change(ViewState.from_payload(json.loads(message))))

    async def close(self):
        if self.ws:
            await self.ws.close()

    def run(self, icon: str):
        try:
            self.loop.run_until_complete(self.start(icon))
        except websockets.ConnectionClosed:
            pass
