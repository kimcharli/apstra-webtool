from fastapi.staticfiles import StaticFiles
from reactpy import component, html
from reactpy.backend.fastapi import configure, Options
from fastapi import Body, FastAPI, Request, UploadFile, Form
import uvicorn
import logging
import os
from typing import Annotated
from pydantic import BaseModel

from webtool.components.apstra_server import ApstraServerComponent, ApstraServer


The_Title = os.environ.get('WEB_TITLE', "Apstra Webtool")
# The_Title = "Apstra Webtool"
options = Options
the_title = [x for x in options.head if x['tagName'] == 'title']
the_title[0]['children'] = [The_Title]

# logging.error(f"after {options.head=}")

app = FastAPI()
app.mount("/public", StaticFiles(directory="webtool/public"), name="public")

config = uvicorn.Config(app, host='localhost', port=8001, log_level='debug', reload=True)



# @app.middleware("http")
# async def disect_request(request: Request, call_next):
#     logging.warning(f"TRACING: request {request.url} {request.headers=}")
#     body = await request.body()
#     logging.warning(f"TRACING: request body {body=}")
#     response = await call_next(request)
#     logging.warning(f"TRACING: response {response}, {type(response)=}")
#     return response


class LoginData(BaseModel):
    host: str
    port: int
    username: str
    password: str

@app.post("/login")
# async def login(host: Annotated[str, Form()], port: Annotated[str, Form()], username: Annotated[str, Form()], password: Annotated[str, Form()]):
async def login(login_data: LoginData):
    """
    login to the server
    """
    try:
        logging.warning(f"login {login_data=}")
        # async for chunk in request.stream():
        #     print(chunk)
        # logging.warning(f"login {host=} {port=} {username=} {password=}")
        version, status = ApstraServer.login(login_data.host, login_data.port, login_data.username, login_data.password)
        logging.warning(f"login {status=} {version=}")
        return {"status": status, "version": version}
    except Exception as e:
        logging.error(f"login {e=}")
        return {"status": str(e), "version": ""}


css_1 = html.link(
        {
        "rel": "stylesheet",
        "href": "/public/style.css"
        }
    )

@component
def home():
    return html.section(
        css_1,
        html.h1("Apstra Webtool"),
        html.hr(),
        ApstraServerComponent(),
        html.hr(),
        html.hr(),
        )

# configure(app, home, options)
configure(app, home)
