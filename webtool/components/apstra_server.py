# import json
# from pathlib import Path
# import asyncio
# import aiohttp
# from dataclasses import dataclass
# from typing import Any, Optional, Tuple

# from reactpy import component, event, hooks, html

# from ck_apstra_api.apstra_session import CkApstraSession


# class ApstraServer:
#     host = None
#     port = None
#     username = None
#     password = None
#     logging_level = 'DEBUG'
#     apstra_server = None  # CkApstraSession

#     @classmethod
#     def login(cls, host, port, username, password) -> Tuple[Optional[CkApstraSession], Optional[Any]]:
#         """
#         Login to the ApstraServer and return version and the error message
#         """
#         cls.apstra_server = CkApstraSession(host, port, username, password)
#         if cls.apstra_server.last_error:
#             return cls.apstra_server.version, cls.apstra_server.last_error
#         cls.host = host
#         cls.port = port
#         cls.username = username
#         cls.password = password
#         return cls.apstra_server.version, "ok"    


# @component
# def ApstraServerComponent():
#     apstra_host, set_apstra_host = hooks.use_state('10.85.192.50')
#     apstra_port, set_apstra_port = hooks.use_state(443)
#     apstra_user, set_apstra_user = hooks.use_state('admin')
#     apstra_password, set_apstra_password = hooks.use_state('zaq1@WSXcde3$RFV')
#     apstra_version, set_apstra_version = hooks.use_state('')
#     apstra_status, set_apstra_status = hooks.use_state('')

#     @event(prevent_default=True)
#     async def handle_login(event):
#         try:
#             async with aiohttp.ClientSession('http://localhost:8000') as session:
#                 async with session.post(
#                     f"/login",
#             # async with aiohttp.ClientSession() as session:
#             #     async with session.post(
#             #         f"http://localhost:8000/login",
#                     json={"host": apstra_host, "port": apstra_port, "username": apstra_user, "password": apstra_password},
#                 ) as response:
#                     # assert await response.status == 200
#                     response.raise_for_status()
#                     data = await response.json()
#                     set_apstra_version(data["version"])
#                     set_apstra_status(data["status"])
#         except Exception as e:
#             set_apstra_status(str(e))

#     return html.form(
#         html.button({"type": "submit", "on_click": handle_login}, "Login"),
#         html.table(
#             {   "style": {"border": "1px solid black"}, 
#                 "class_name": "border1"
#             },
#             html.tr(
#                 html.th("Version"),
#                 html.th("Status"),
#                 html.th("Host"),
#                 html.th("Port"),
#                 html.th("User"),
#                 html.th("Password"),
#             ),
#             html.tr(
#                 html.td(
#                     html.label(apstra_version)
#                 ),
#                 html.td(
#                     html.label(apstra_status)
#                 ),
#                 html.td(
#                     html.input(
#                         {
#                             "type": "text",
#                             "placeholder": "Apstra Host",
#                             "value": apstra_host,
#                             "on_change": lambda event: set_apstra_host(event["target"]["value"]),
#                         }
#                     ),
#                 ),
#                 html.td(
#                     html.input(
#                         {
#                             "type": "number",
#                             "placeholder": "Apstra Port",
#                             "value": apstra_port,
#                             "on_change": lambda event: set_apstra_port(event["target"]["value"]),
#                         }
#                     ),
#                 ),
#                 html.td(
#                     html.input(
#                         {
#                             "type": "text",
#                             "placeholder": "Apstra User",
#                             "value": apstra_user,
#                             "on_change": lambda event: set_apstra_user(event["target"]["value"]),
#                         }
#                     ),
#                 ),
#                 html.td(
#                     html.input(
#                         {
#                             "type": "password",
#                             "placeholder": "Apstra Password",
#                             "value": apstra_password,
#                             "on_change": lambda event: set_apstra_password(event["target"]["value"]),
#                         }
#                     ),
#                 ),
#             )
#         )
#     )

from typing import Any, Optional, Tuple
from dataclasses import dataclass
import httpx
from contextlib import contextmanager
from nicegui import ui
import logging

from ck_apstra_api.apstra_session import CkApstraSession

@dataclass
class ApstraServer:
    host: str = '10.85.192.50'
    port: str = '443'
    username: str = 'admin'
    password: str =  'zaq1@WSXcde3$RFV'
    logging_level = 'DEBUG'
    # apstra_server = None  # CkApstraSession
    version: str = 'NA'
    status: str = 'not connected'

    # @classmethod
    # def login(self, host, port, username, password) -> Tuple[Optional[CkApstraSession], Optional[Any]]:
    def login(self) -> Tuple[Optional[CkApstraSession], Optional[Any]]:
        """
        Login to the ApstraServer and return version and the error message
        """
        # self.apstra_server = CkApstraSession(host, port, username, password)
        self.apstra_server = CkApstraSession(self.host, self.port, self.username, self.password)
        self.version = self.apstra_server.version
        self.status = self.apstra_server.last_error or "ok"
        if self.apstra_server.last_error:
            return self.apstra_server.version, self.apstra_server.last_error
        # self.host = host
        # self.port = port
        # self.username = username
        # self.password = password
        logging.warning(f"ApstraServer::login {ApstraServer=}")
        return self.apstra_server.version, "ok"    

# global variable
apstra_server = ApstraServer()

@contextmanager
def disable(button: ui.button):
    button.disable()
    try:
        yield
    finally:
        button.enable()

async def login(button: ui.button) -> None:
    with disable(button):
        async with httpx.AsyncClient() as client:
            response = await client.get('http://localhost:8000/login')
            # response = await client.post('http://localhost:8000/login', json={
            #     'host': apstra_server.host,
            #     'port': apstra_server.port,
            #     'username': apstra_server.username,
            #     'password': apstra_server.password,
            # })
            ui.notify(f'Response code: {response.status_code}')





def content() -> None:
    global apstra_server
    with ui.grid(columns=6).classes('w-full gap-0'):
        ui.label('Version').classes('font-bold border p-1')
        ui.label('Status').classes('font-bold border p-1')
        ui.label('Host').classes('font-bold border p-1')
        ui.label('Port').classes('font-bold border p-1')
        ui.label('Username').classes('font-bold border p-1')
        ui.label('Password').classes('font-bold border p-1')

        ui.input().classes('border p-1').bind_value(apstra_server, 'version')
        ui.input().classes('border p-1').bind_value(apstra_server, 'status')
        ui.input().classes('border p-1').bind_value(apstra_server, 'host')
        ui.input().classes('border p-1').bind_value(apstra_server, 'port')
        ui.input().classes('border p-1').bind_value(apstra_server, 'username')
        ui.input(password=True, password_toggle_button=True).classes('border p-1').bind_value(apstra_server, 'password')

        with ui.button(on_click=lambda e: login(e.sender)):
            ui.label('Login')
            ui.image('/public/login.svg').classes('rounded-full w-8 h-8 ml-4')
            # ui.button('Login', on_click=lambda: ui.notify('Login clicked')).classes('col-span-6 text-white bg-blue-500 border p-1')
