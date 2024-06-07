import json
from pathlib import Path
import asyncio
from dataclasses import dataclass
from typing import Any, Optional, Tuple
import logging

from webtool.components.socket import sio, SocketEnum

from ck_apstra_api.apstra_session import CkApstraSession

logger = logging.getLogger('apstra_server')


@sio.on(SocketEnum.LOGIN)
async def apstra_login(sid, login_data):
    logger.warning(f"login begin: {sid} connected, {login_data=}")
    version, status = await apstra_server.login(login_data)
    await sio.emit('login', {'version': version, 'status': status}, room=sid)
    logger.warning(f"login end: {sid} connected, {login_data=}")


@sio.on(SocketEnum.LOGOUT)
async def apstra_logout(sid):
    logger.warning(f"logout begin: {sid} connected")
    await apstra_server.logout()
    await sio.emit('logout', {'status': 'ok'})
    logger.warning(f"logout end: {sid} connected")
    
@dataclass
class ApstraServer:
    host: str = '10.85.192.45'
    port: str = '443'
    username: str = 'admin'
    password: str =  'admin'
    logging_level = 'DEBUG'
    apstra_server: Any = None  # CkApstraSession
    version: str = 'NA'
    status: str = 'not connected'

    async def login(self, data: dict):
        """
        Login to the ApstraServer and return version and the error message
        """
        # self.apstra_server = CkApstraSession(host, port, username, password)
        self.host = data['host']
        self.port = data['port']
        self.username = data['username']
        self.password = data['password']
        self.apstra_server = CkApstraSession(self.host, self.port, self.username, self.password)
        self.version = self.apstra_server.version
        self.status = self.apstra_server.last_error or "ok"
        if self.apstra_server.last_error:
            return self.apstra_server.version, self.apstra_server.last_error
        logging.warning(f"ApstraServer::login {ApstraServer=}")
        return self.apstra_server.version, "ok"    

    async def logout(self):
        """
        Logout from the ApstraServer
        """
        self.apstra_server.logout()
        self.status = 'not connected'
        logging.warning(f"ApstraServer::logout {ApstraServer=}")

# global variable
apstra_server = ApstraServer()



