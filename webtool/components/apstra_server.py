import json
from pathlib import Path
import asyncio
from dataclasses import dataclass
from typing import Any, Optional, Tuple
import logging

from ck_apstra_api.apstra_session import CkApstraSession


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

    def login(self, data: dict):
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

# global variable
apstra_server = ApstraServer()


