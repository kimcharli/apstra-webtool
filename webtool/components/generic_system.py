# import json
# from pathlib import Path
# import asyncio
# import logging
# import aiohttp
# from dataclasses import dataclass
# from typing import Any, Optional, Tuple

# from fastapi import Body, FastAPI, Request, UploadFile, Form

# from reactpy import component, event, hooks, html

# from ck_apstra_api.apstra_session import CkApstraSession


# class GenericSystem:
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

# # # @event(prevent_default=True)
# # async def upload_file(event):
# #     file = GenericSystemUpload.state.file
# #     form_data = FormData()
# #     form_data.append("file", file)
# #     async with aiohttp.ClientSession('http://localhost:8000') as session:
# #         async with session.post(
# #             f"/upload-xlsx",
# #             files = form_data,
# #         ) as response:
# #             assert response.status == 200
# #             logging.warning(f"upload_file {response=}")

#     # try:
#     #     async with aiohttp.ClientSession('http://localhost:8000') as session:
#     #         async with session.post(
#     #             f"/upload-xlsx",
#     #     # async with aiohttp.ClientSession() as session:
#     #     #     async with session.post(
#     #     #         f"http://localhost:8000/login",
#     #             json={"host": apstra_host, "port": apstra_port, "username": apstra_user, "password": apstra_password},
#     #         ) as response:
#     #             # assert await response.status == 200
#     #             response.raise_for_status()
#     #             data = await response.json()
#     #             set_apstra_version(data["version"])
#     #             set_apstra_status(data["status"])
#     # except Exception as e:
#     #     set_apstra_status(str(e))


# eventx={
#     'bubbles': True, 
#     'composed': False, 
#     'currentTarget': {
#         'tagName': 'INPUT', 
#         'boundingClientRect': {}, 
#         'value': 'C:\\fakepath\\sample.xlsx'}, 
#         'defaultPrevented': False, 
#         'eventPhase': 2, 
#         'isTrusted': True, 
#         'target': {
#             'tagName': 'INPUT', 
#             'boundingClientRect': {}, 
#             'value': 'C:\\fakepath\\sample.xlsx'}, 
#             'timeStamp': 408406.5, 
#             'type': 'change', 
#             'selection': None}

# @component
# def GenericSystemUploadComponent():
#     file, set_file = hooks.use_state(None)
#     msg, set_msg = hooks.use_state("msg")

#     @event(prevent_default=True)
#     async def handle_change(event):
#         logging.warning(f"GenericSystemUploadComponent::handle_change begin {event=}")
#         set_msg("handle_change " + str(event))
#         set_msg(msg + "handle_change " + str(event['currentTarget']))
#         # logging.warning(f"GenericSystemUploadComponent::handle_change begin {event.currentTarget=}")
#         # set_file = event.target.files[0]

#     @event(prevent_default=True)
#     async def upload_file(event):
#         logging.warning(f"GenericSystemUploadComponent::upload_file begin {event=}")
#         set_msg("upload_file " + str(event))


#     # @event(prevent_default=True)
#     # async def handleFileUpload(event):
#     #     logging.warning(f"GenericSystemUploadComponent::handleFileUpload begin {event=}")
#     #     logging.warning(f"GenericSystemUploadComponent::handleFileUpload begin {event.currentTarget=}")
#     #     file = event.target.files[0]
#     #     set_file(file)
#     #     try:
#     #         async with aiohttp.ClientSession('http://localhost:8000') as session:
#     #             async with session.post(
#     #                 f"/upload-xlsx",
#     #         # async with aiohttp.ClientSession() as session:
#     #         #     async with session.post(
#     #         #         f"http://localhost:8000/login",
#     #                 body=file,
#     #             ) as response:
#     #                 # assert await response.status == 200
#     #                 set_msg(msg + f" {response=}")
#     #                 response.raise_for_status()
#     #                 data = await response.json()
#     #     except Exception as e:
#     #         logging.error(f"handleFileUpload {e=}")

#     # return html.div(
#     #     html.input({
#     #         "type": "file",
#     #         "accept": ".xlsx",
#     #         "on_change": handle_change
#     #     }),
#     #     html.br(),
#     #     html.button({"type": "submit", "on_click": upload_file}, "Upload XLSX"),
#     #     html.br(),
#     #     html.a({"href": "/public/sample.xlsx", "download": ""},
#     #                 "Download Sample"),
#     #     html.br(),
#     #     html.label(msg),
#     #     html.br(),
#     # )

#     return html.form(
#         {   "method": "post",
#             "enctype": "multipart/form-data",
#             "action": "/upload-xlsx",
#             },
#         html.input({
#             "type": "file",
#             "accept": ".xlsx",
#             "name": "file",
#             # "on_change": handle_change
#         }),
#         html.button({"type": "submit", "on_click": upload_file}, "Upload XLSX"),
#         html.button({"type": "submit", "on_click": upload_file}, "Upload XLSX"),
#         html.br(),
#         html.a({"href": "/public/sample.xlsx", "download": ""},
#                     "Download Sample"),
#         html.br(),
#         html.textarea(

#         ),
#         html.table(
#             {"style": {"border": "1px solid black"}},
#             # html.tr(
#             #     html.th("Version"),
#             #     html.th("Status"),
#             #     html.th("Host"),
#             #     html.th("Port"),
#             #     html.th("User"),
#             #     html.th("Password"),
#             # ),
#             # html.tr(
#             #     html.td(
#             #         html.label(apstra_version)
#             #     ),
#             #     html.td(
#             #         html.label(apstra_status)
#             #     ),
#             #     html.td(
#             #         html.input(
#             #             {
#             #                 "type": "text",
#             #                 "placeholder": "Apstra Host",
#             #                 "value": apstra_host,
#             #                 "on_change": lambda event: set_apstra_host(event["target"]["value"]),
#             #             }
#             #         ),
#             #     ),
#             #     html.td(
#             #         html.input(
#             #             {
#             #                 "type": "number",
#             #                 "placeholder": "Apstra Port",
#             #                 "value": apstra_port,
#             #                 "on_change": lambda event: set_apstra_port(event["target"]["value"]),
#             #             }
#             #         ),
#             #     ),
#             #     html.td(
#             #         html.input(
#             #             {
#             #                 "type": "text",
#             #                 "placeholder": "Apstra User",
#             #                 "value": apstra_user,
#             #                 "on_change": lambda event: set_apstra_user(event["target"]["value"]),
#             #             }
#             #         ),
#             #     ),
#             #     html.td(
#             #         html.input(
#             #             {
#             #                 "type": "password",
#             #                 "placeholder": "Apstra Password",
#             #                 "value": apstra_password,
#             #                 "on_change": lambda event: set_apstra_password(event["target"]["value"]),
#             #             }
#             #         ),
#             #     ),
#             # )
#         )
#     )



# from typing import Any, Optional, Tuple
# from dataclasses import dataclass
# import httpx
# from contextlib import contextmanager
# from nicegui import ui
# import logging

# from ck_apstra_api.apstra_session import CkApstraSession

# @dataclass
# class ApstraServer:
#     host: str = '10.85.192.50'
#     port: str = '443'
#     username: str = 'admin'
#     password: str =  'zaq1@WSXcde3$RFV'
#     logging_level = 'DEBUG'
#     # apstra_server = None  # CkApstraSession
#     version: str = 'NA'
#     status: str = 'not connected'

#     # @classmethod
#     # def login(self, host, port, username, password) -> Tuple[Optional[CkApstraSession], Optional[Any]]:
#     def login(self) -> Tuple[Optional[CkApstraSession], Optional[Any]]:
#         """
#         Login to the ApstraServer and return version and the error message
#         """
#         # self.apstra_server = CkApstraSession(host, port, username, password)
#         self.apstra_server = CkApstraSession(self.host, self.port, self.username, self.password)
#         self.version = self.apstra_server.version
#         self.status = self.apstra_server.last_error or "ok"
#         if self.apstra_server.last_error:
#             return self.apstra_server.version, self.apstra_server.last_error
#         # self.host = host
#         # self.port = port
#         # self.username = username
#         # self.password = password
#         logging.warning(f"ApstraServer::login {ApstraServer=}")
#         return self.apstra_server.version, "ok"    

# # global variable
# apstra_server = ApstraServer()

# @contextmanager
# def disable(button: ui.button):
#     button.disable()
#     try:
#         yield
#     finally:
#         button.enable()

# async def login(button: ui.button) -> None:
#     with disable(button):
#         async with httpx.AsyncClient() as client:
#             response = await client.get('http://localhost:8000/login')
#             # response = await client.post('http://localhost:8000/login', json={
#             #     'host': apstra_server.host,
#             #     'port': apstra_server.port,
#             #     'username': apstra_server.username,
#             #     'password': apstra_server.password,
#             # })
#             ui.notify(f'Response code: {response.status_code}')





# def content() -> None:
#     global apstra_server
#     with ui.grid(columns=6).classes('w-full gap-0'):
#         ui.label('Version').classes('font-bold border p-1')
#         ui.label('Status').classes('font-bold border p-1')
#         ui.label('Host').classes('font-bold border p-1')
#         ui.label('Port').classes('font-bold border p-1')
#         ui.label('Username').classes('font-bold border p-1')
#         ui.label('Password').classes('font-bold border p-1')

#         ui.input().classes('border p-1').bind_value(apstra_server, 'version')
#         ui.input().classes('border p-1').bind_value(apstra_server, 'status')
#         ui.input().classes('border p-1').bind_value(apstra_server, 'host')
#         ui.input().classes('border p-1').bind_value(apstra_server, 'port')
#         ui.input().classes('border p-1').bind_value(apstra_server, 'username')
#         ui.input(password=True, password_toggle_button=True).classes('border p-1').bind_value(apstra_server, 'password')

#         with ui.button(on_click=lambda e: login(e.sender)):
#             ui.label('Login')
#             ui.image('/public/login.svg').classes('rounded-full w-8 h-8 ml-4')
#             # ui.button('Login', on_click=lambda: ui.notify('Login clicked')).classes('col-span-6 text-white bg-blue-500 border p-1')
    
#     ui.separator()


from typing import Dict
from nicegui import ui, events
import logging
import pandas as pd
from io import StringIO


# def handle_upload(e: events.UploadEventArguments) -> None:
#     logging.warning(f"handle_upload {e=}")
#     logging.warning(f"handle_upload {e.content=}")
#     # with StringIO(e.content.read().decode('utf-8')) as f:
#     with StringIO(e.content.read().decode('mac_roman')) as f:
#     # with StringIO(e.content.read().decode('unicode_escape')) as f:
#         # df = pd.read_excel(f, encoding='unicode_escape')
#         df = pd.read_excel(f, sheet_name='generic_systems')
#         # logging.warning(f"handle_upload {df=}")
#     ui.table(columns=[{"name": col, "label": col, "field": col} for col in df.columns], rows=[{col: row[col] for col in df.columns} for _, row in df.iterrows()])
#     # df = pd.read_excel(e.content.read().decode('utf-8'))
#     # text = e.content.read().decode('utf-8')
#     # content.set_context(text)
#     # dialog.open()

the_columns = []
the_rows = []
the_ui_table = None
the_select_columns = None

def handle_csv_upload(e: events.UploadEventArguments) -> None:
    global the_columns, the_rows, the_ui_table, the_select_columns
    with StringIO(e.content.read().decode('utf-8')) as f:
        df = pd.read_csv(f) 
    the_columns=[{"name": col, "label": col, "field": col} for col in df.columns]
    the_rows=[{col: row[col] for col in df.columns} for _, row in df.iterrows()]
    the_ui_table = ui.table(columns=the_columns, rows=the_rows)

    # def toggle(column: Dict, visible: bool) -> None:
    #     column['classes'] = '' if visible else 'hidden'
    #     column['headerClasses'] = '' if visible else 'hidden'
    #     the_table.update()

    with ui.button('Columns', icon='menu'):
        with ui.menu(), ui.column().classes('gap-0 p-2'):
            for column in the_columns:
                ui.switch(column['label'], value=True, on_change=lambda e,
                        column=column: toggle(column, e.value))

    # if the_select_columns is not None:
    #     the_select_columns.delete()
    # the_select_columns = None
    # the_select_columns = ui.button('Columns', on_click=select_columns)
    # with the_select_columns:
    #     with ui.menu(), ui.column().classes('gap-0 p-2'):
    #         for column in the_columns:
    #             ui.switch(column['label'], value=True, on_change=lambda e,
    #                     column=column: toggle(column, e.value))


def toggle(column: Dict, visible: bool) -> None:
    column['classes'] = '' if visible else 'hidden'
    column['headerClasses'] = '' if visible else 'hidden'
    the_ui_table.update()
    return

def select_columns() -> None:
    global the_columns
    with ui.button('Columns', icon='menu'):
        with ui.menu(), ui.column().classes('gap-0 p-2'):
            for column in the_columns:
                ui.switch(column['label'], value=True, on_change=lambda e,
                        column=column: toggle(column, e.value))

def clear_table() -> None:
    global the_ui_table
    the_ui_table.delete()
    the_select_columns.delete()


def content() -> None:
    global the_columns
    # ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('max-w-full').props('accept=.xlsx')

    # ui.upload(on_upload=handle_upload, label="xlsx upload").props('accept=.xlsx')
    ui.label('Generic System')
    with ui.row():
        ui.upload(on_upload=handle_csv_upload, label="csv upload", auto_upload=True).props('accept=.csv')
        # # select_columns()
        # with ui.button('Columns', icon='menu'):
        #     with ui.menu(), ui.column().classes('gap-0 p-2'):
        #         for column in the_columns:
        #             ui.switch(column['label'], value=True, on_change=lambda e,
        #                     column=column: toggle(column, e.value))
        ui.button('Clear Table', on_click=clear_table)

