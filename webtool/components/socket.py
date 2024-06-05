import socketio

# broadcast = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

socket_app = socketio.ASGIApp(sio)


