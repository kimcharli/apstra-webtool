import json
import logging
import asyncio

from fastapi import FastAPI, HTTPException, Request, Form, WebSocket, Cookie, Query, WebSocketDisconnect
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

# from webtool.components.sse import sse_queue, sse_logging


logger = logging.getLogger('webtool.main')
app = FastAPI()

app.mount("/static", StaticFiles(directory="webtool/static"), name="static")
app.mount("/js", StaticFiles(directory="webtool/static/js"), name="js")
app.mount("/css", StaticFiles(directory="webtool/static/css"), name="css")
app.mount("/images", StaticFiles(directory="webtool/static/images"), name="images")



class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    client_id = 1
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            d1 = json.loads(data)
            logging.warning(f"######## websocket_endpoint {data=} {type(data)} {dir(data)=}")
            if 'login' in d1:
                logging.warning(f"######## websocket_endpoint {d1=} {type(d1)} {d1['login']=}")
            await manager.send_personal_message(f"You wrote: {data=} {type(data)}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")


@app.get("/", response_class=HTMLResponse)
async def get_index_html(request: Request):
    return FileResponse("webtool/static/index.html")


