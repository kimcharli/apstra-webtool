import socketio
from enum import StrEnum
import logging

logger = logging.getLogger('socket')

class SocketEnum(StrEnum):
    CONNECT = 'connect'
    DISCONNECT = 'disconnect'
    LOGIN = 'login'
    LOGOUT = 'logout'

# broadcast = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

socket_app = socketio.ASGIApp(sio)

@sio.on('connect')
async def connect(sid, environ):
    logger.warning(f"Client {sid} connected")

@sio.on('disconnect')
async def disconnect(sid):
    logger.warning(f"Client {sid} disconnected")

@sio.on('*')
async def catch_all(event, sid, data):
    logger.warning(f"catch_all({event},{sid},{data}) {type(event)=}")
    await sio.emit('msg', data)