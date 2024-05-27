import json
import logging
from typing import Any
from dataclasses import asdict, dataclass
import asyncio


sse_queue = asyncio.Queue()


@dataclass
class SseEvent:
    event: str
    data: Any = None

    async def send(self):
        await asyncio.sleep(0.05)
        try:
            if self.event == 'log':
                sse_dict = {'event': self.event, 'data': self.data}
            else:
                sse_dict = {'event': self.event, 'data': json.dumps(asdict(self.data))}
            await sse_queue.put(sse_dict)
        except Exception as e:
            logging.error(f"send_sse_event: {e=} {self}")

async def sse_logging(log: str):
    await SseEvent('log', log).send()
