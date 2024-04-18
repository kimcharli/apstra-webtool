import json
from pathlib import Path
import asyncio
import logging
import aiohttp
from dataclasses import dataclass
from typing import Any, Optional, Tuple

from fastapi import Body, FastAPI, Request, UploadFile, Form

from reactpy import component, event, hooks, html

from ck_apstra_api.apstra_session import CkApstraSession


class GenericSystem:
    host = None
    port = None
    username = None
    password = None
    logging_level = 'DEBUG'
    apstra_server = None  # CkApstraSession

    @classmethod
    def login(cls, host, port, username, password) -> Tuple[Optional[CkApstraSession], Optional[Any]]:
        """
        Login to the ApstraServer and return version and the error message
        """
        cls.apstra_server = CkApstraSession(host, port, username, password)
        if cls.apstra_server.last_error:
            return cls.apstra_server.version, cls.apstra_server.last_error
        cls.host = host
        cls.port = port
        cls.username = username
        cls.password = password
        return cls.apstra_server.version, "ok"    

# # @event(prevent_default=True)
# async def upload_file(event):
#     file = GenericSystemUpload.state.file
#     form_data = FormData()
#     form_data.append("file", file)
#     async with aiohttp.ClientSession('http://localhost:8000') as session:
#         async with session.post(
#             f"/upload-xlsx",
#             files = form_data,
#         ) as response:
#             assert response.status == 200
#             logging.warning(f"upload_file {response=}")

    # try:
    #     async with aiohttp.ClientSession('http://localhost:8000') as session:
    #         async with session.post(
    #             f"/upload-xlsx",
    #     # async with aiohttp.ClientSession() as session:
    #     #     async with session.post(
    #     #         f"http://localhost:8000/login",
    #             json={"host": apstra_host, "port": apstra_port, "username": apstra_user, "password": apstra_password},
    #         ) as response:
    #             # assert await response.status == 200
    #             response.raise_for_status()
    #             data = await response.json()
    #             set_apstra_version(data["version"])
    #             set_apstra_status(data["status"])
    # except Exception as e:
    #     set_apstra_status(str(e))


eventx={
    'bubbles': True, 
    'composed': False, 
    'currentTarget': {
        'tagName': 'INPUT', 
        'boundingClientRect': {}, 
        'value': 'C:\\fakepath\\sample.xlsx'}, 
        'defaultPrevented': False, 
        'eventPhase': 2, 
        'isTrusted': True, 
        'target': {
            'tagName': 'INPUT', 
            'boundingClientRect': {}, 
            'value': 'C:\\fakepath\\sample.xlsx'}, 
            'timeStamp': 408406.5, 
            'type': 'change', 
            'selection': None}

@component
def GenericSystemUploadComponent():
    file, set_file = hooks.use_state(None)
    msg, set_msg = hooks.use_state("msg")

    @event(prevent_default=True)
    async def handle_change(event):
        logging.warning(f"GenericSystemUploadComponent::handle_change begin {event=}")
        set_msg("handle_change " + str(event))
        set_msg(msg + "handle_change " + str(event['currentTarget']))
        # logging.warning(f"GenericSystemUploadComponent::handle_change begin {event.currentTarget=}")
        # set_file = event.target.files[0]

    @event(prevent_default=True)
    async def upload_file(event):
        logging.warning(f"GenericSystemUploadComponent::upload_file begin {event=}")
        set_msg("upload_file " + str(event))


    # @event(prevent_default=True)
    # async def handleFileUpload(event):
    #     logging.warning(f"GenericSystemUploadComponent::handleFileUpload begin {event=}")
    #     logging.warning(f"GenericSystemUploadComponent::handleFileUpload begin {event.currentTarget=}")
    #     file = event.target.files[0]
    #     set_file(file)
    #     try:
    #         async with aiohttp.ClientSession('http://localhost:8000') as session:
    #             async with session.post(
    #                 f"/upload-xlsx",
    #         # async with aiohttp.ClientSession() as session:
    #         #     async with session.post(
    #         #         f"http://localhost:8000/login",
    #                 body=file,
    #             ) as response:
    #                 # assert await response.status == 200
    #                 set_msg(msg + f" {response=}")
    #                 response.raise_for_status()
    #                 data = await response.json()
    #     except Exception as e:
    #         logging.error(f"handleFileUpload {e=}")

    # return html.div(
    #     html.input({
    #         "type": "file",
    #         "accept": ".xlsx",
    #         "on_change": handle_change
    #     }),
    #     html.br(),
    #     html.button({"type": "submit", "on_click": upload_file}, "Upload XLSX"),
    #     html.br(),
    #     html.a({"href": "/public/sample.xlsx", "download": ""},
    #                 "Download Sample"),
    #     html.br(),
    #     html.label(msg),
    #     html.br(),
    # )

    return html.form(
        {   "method": "post",
            "enctype": "multipart/form-data",
            "action": "/upload-xlsx",
            },
        html.input({
            "type": "file",
            "accept": ".xlsx",
            "name": "file",
            # "on_change": handle_change
        }),
        html.button({"type": "submit", "on_click": upload_file}, "Upload XLSX"),
        html.button({"type": "submit", "on_click": upload_file}, "Upload XLSX"),
        html.br(),
        html.a({"href": "/public/sample.xlsx", "download": ""},
                    "Download Sample"),
        html.br(),
        html.textarea(

        ),
        html.table(
            {"style": {"border": "1px solid black"}},
            # html.tr(
            #     html.th("Version"),
            #     html.th("Status"),
            #     html.th("Host"),
            #     html.th("Port"),
            #     html.th("User"),
            #     html.th("Password"),
            # ),
            # html.tr(
            #     html.td(
            #         html.label(apstra_version)
            #     ),
            #     html.td(
            #         html.label(apstra_status)
            #     ),
            #     html.td(
            #         html.input(
            #             {
            #                 "type": "text",
            #                 "placeholder": "Apstra Host",
            #                 "value": apstra_host,
            #                 "on_change": lambda event: set_apstra_host(event["target"]["value"]),
            #             }
            #         ),
            #     ),
            #     html.td(
            #         html.input(
            #             {
            #                 "type": "number",
            #                 "placeholder": "Apstra Port",
            #                 "value": apstra_port,
            #                 "on_change": lambda event: set_apstra_port(event["target"]["value"]),
            #             }
            #         ),
            #     ),
            #     html.td(
            #         html.input(
            #             {
            #                 "type": "text",
            #                 "placeholder": "Apstra User",
            #                 "value": apstra_user,
            #                 "on_change": lambda event: set_apstra_user(event["target"]["value"]),
            #             }
            #         ),
            #     ),
            #     html.td(
            #         html.input(
            #             {
            #                 "type": "password",
            #                 "placeholder": "Apstra Password",
            #                 "value": apstra_password,
            #                 "on_change": lambda event: set_apstra_password(event["target"]["value"]),
            #             }
            #         ),
            #     ),
            # )
        )
    )


