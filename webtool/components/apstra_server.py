import json
from pathlib import Path
import asyncio
import aiohttp
from dataclasses import dataclass
from typing import Any, Optional, Tuple

from reactpy import component, event, hooks, html

from ck_apstra_api.apstra_session import CkApstraSession


class ApstraServer:
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


@component
def ApstraServerComponent():
    apstra_host, set_apstra_host = hooks.use_state('10.85.192.50')
    apstra_port, set_apstra_port = hooks.use_state(443)
    apstra_user, set_apstra_user = hooks.use_state('admin')
    apstra_password, set_apstra_password = hooks.use_state('zaq1@WSXcde3$RFV')
    apstra_version, set_apstra_version = hooks.use_state('')
    apstra_status, set_apstra_status = hooks.use_state('')

    @event(prevent_default=True)
    async def handle_login(event):
        try:
            async with aiohttp.ClientSession('http://localhost:8000') as session:
                async with session.post(
                    f"/login",
            # async with aiohttp.ClientSession() as session:
            #     async with session.post(
            #         f"http://localhost:8000/login",
                    json={"host": apstra_host, "port": apstra_port, "username": apstra_user, "password": apstra_password},
                ) as response:
                    # assert await response.status == 200
                    response.raise_for_status()
                    data = await response.json()
                    set_apstra_version(data["version"])
                    set_apstra_status(data["status"])
        except Exception as e:
            set_apstra_status(str(e))

    return html.form(
        html.button({"type": "submit", "on_click": handle_login}, "Login"),
        html.table(
            {"style": {"border": "1px solid black"}},
            html.tr(
                html.th("Version"),
                html.th("Status"),
                html.th("Host"),
                html.th("Port"),
                html.th("User"),
                html.th("Password"),
            ),
            html.tr(
                html.td(
                    html.label(apstra_version)
                ),
                html.td(
                    html.label(apstra_status)
                ),
                html.td(
                    html.input(
                        {
                            "type": "text",
                            "placeholder": "Apstra Host",
                            "value": apstra_host,
                            "on_change": lambda event: set_apstra_host(event["target"]["value"]),
                        }
                    ),
                ),
                html.td(
                    html.input(
                        {
                            "type": "number",
                            "placeholder": "Apstra Port",
                            "value": apstra_port,
                            "on_change": lambda event: set_apstra_port(event["target"]["value"]),
                        }
                    ),
                ),
                html.td(
                    html.input(
                        {
                            "type": "text",
                            "placeholder": "Apstra User",
                            "value": apstra_user,
                            "on_change": lambda event: set_apstra_user(event["target"]["value"]),
                        }
                    ),
                ),
                html.td(
                    html.input(
                        {
                            "type": "password",
                            "placeholder": "Apstra Password",
                            "value": apstra_password,
                            "on_change": lambda event: set_apstra_password(event["target"]["value"]),
                        }
                    ),
                ),
            )
        )
    )


