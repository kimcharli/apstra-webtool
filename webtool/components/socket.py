import socketio
from enum import StrEnum
import logging

logger = logging.getLogger('socket')

class SocketEnum(StrEnum):
    CONNECT = 'connect'
    DISCONNECT = 'disconnect'
    LOGIN = 'login'
    LOGOUT = 'logout'
    GS_SAMPLE = 'gs_sample'

# broadcast = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

socket_app = socketio.ASGIApp(sio)

@sio.on(SocketEnum.CONNECT)
async def connect(sid, environ):
    logger.warning(f"Client {sid} connected")

@sio.on(SocketEnum.DISCONNECT)
async def disconnect(sid):
    logger.warning(f"Client {sid} disconnected")


@sio.on('create-something')
async def create_something(sid, data):
    logger.warning(f"Client {sid} created something: {data}")
    await sio.emit('something-created', data)

@sio.on('msg')
async def handle_msg(sid, data):
    logger.warning(f"handle_msg({sid},{data})")
    await sio.emit('msg', data)

@sio.on('send_msg')
async def handle_send_msg(sid, data):
    logger.warning(f"handle_send_msg({sid}, {data})")
    await sio.emit('msg', data)


@sio.on('*')
async def catch_all(event, sid, data):
    logger.warning(f"catch_all({event},{sid},{data}) {type(event)=}")
    await sio.emit('msg', data)