# from fastapi.staticfiles import StaticFiles
# from reactpy import component, html
# from reactpy.backend.fastapi import configure, Options
# from fastapi import Body, FastAPI, Request, UploadFile, Form, WebSocket
# from starlette.websockets import WebSocketDisconnect
# from fastapi.responses import HTMLResponse
# import uvicorn
# import logging
# import os
# from typing import Annotated
# from pydantic import BaseModel

# from webtool.components.apstra_server import ApstraServerComponent, ApstraServer
# from webtool.components.generic_system import GenericSystemUploadComponent


# The_Title = os.environ.get('WEB_TITLE', "Apstra Webtool")
# # The_Title = "Apstra Webtool"
# options = Options
# the_title = [x for x in options.head if x['tagName'] == 'title']
# the_title[0]['children'] = [The_Title]

# # logging.error(f"after {options.head=}")

# app = FastAPI()
# app.mount("/public", StaticFiles(directory="webtool/public"), name="public")

# config = uvicorn.Config(app, host='localhost', port=8001, log_level='debug', reload=True)



# # @app.middleware("http")
# # async def disect_request(request: Request, call_next):
# #     logging.warning(f"TRACING: request {request.url} {request.headers=}")
# #     body = await request.body()
# #     logging.warning(f"TRACING: request body {body=}")
# #     response = await call_next(request)
# #     logging.warning(f"TRACING: response {response}, {type(response)=}")
# #     return response


# class LoginData(BaseModel):
#     host: str
#     port: int
#     username: str
#     password: str

# @app.post("/login")
# # async def login(host: Annotated[str, Form()], port: Annotated[str, Form()], username: Annotated[str, Form()], password: Annotated[str, Form()]):
# async def login(login_data: LoginData):
#     """
#     login to the server
#     """
#     try:
#         logging.warning(f"login {login_data=}")
#         # async for chunk in request.stream():
#         #     print(chunk)
#         # logging.warning(f"login {host=} {port=} {username=} {password=}")
#         version, status = ApstraServer.login(login_data.host, login_data.port, login_data.username, login_data.password)
#         logging.warning(f"login {status=} {version=}")
#         return {"status": status, "version": version}
#     except Exception as e:
#         logging.error(f"login {e=}")
#         return {"status": str(e), "version": ""}


# @app.post("/upload-xlsx")
# async def upload_xlsx(request: Request, file: UploadFile):
#     """
#     take environment yaml file to init global_store
#     """
#     logging.warning(f"upload_xlsx {file.filename=}")
#     file_content = await file.read()
#     return {"status": "ok", "version": "1.0"}




# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     try:
#         while True:
#             data = await websocket.receive_text()
#             await websocket.send_text(f"Message text was: {data}")
#     except WebSocketDisconnect as e:
#         logging.warning(f"websocket closed, {e=}")
#         return


# css_1 = html.link(
#         {
#         "rel": "stylesheet",
#         "href": "/public/style.css"
#         }
#     )


# html = """
# <!DOCTYPE html>
# <html>
#     <head>
#         <title>Chat</title>
#     </head>
#     <body>
#         <h1>WebSocket Chat</h1>
#         <form action="" onsubmit="sendMessage(event)">
#             <input type="text" id="messageText" autocomplete="off"/>
#             <button>Send</button>
#         </form>
#         <ul id='messages'>
#         </ul>
#         <script>
#             var ws = new WebSocket("ws://localhost:8000/ws");
#             ws.onmessage = function(event) {
#                 var messages = document.getElementById('messages')
#                 var message = document.createElement('li')
#                 var content = document.createTextNode(event.data)
#                 message.appendChild(content)
#                 messages.appendChild(message)
#             };
#             function sendMessage(event) {
#                 var input = document.getElementById("messageText")
#                 ws.send(input.value)
#                 input.value = ''
#                 event.preventDefault()
#             }
#         </script>
#     </body>
# </html>
# """

# @app.get("/")
# async def get():
#     return HTMLResponse(html)

# # @component
# # def home():
# #     return html.section(
# #         css_1,
# #         html.h1("Apstra Webtool"),
# #         html.hr(),
# #         ApstraServerComponent(),
# #         html.hr(),
# #         GenericSystemUploadComponent(),
# #         html.hr(),
# #         )

# # configure(app, home, options)
# # configure(app, home)



# #!/usr/bin/env python3
# from webtool.components import frontend
# from fastapi import FastAPI

# app = FastAPI()


# @app.get('/')
# def read_root():
#     return {'Hello': 'NiceGUI!'}


# frontend.init(app)

# if __name__ == '__main__':
#     print('Please start the app with the "uvicorn" command as shown in the start.sh script')


from fastapi.staticfiles import StaticFiles
from nicegui import app, ui
from dataclasses import dataclass
import logging

from webtool.components import all_pages
from webtool.components import home_page
from webtool.components import theme

from webtool.components import apstra_server

from fastapi import FastAPI, Request
app = FastAPI()
app.mount("/public", StaticFiles(directory="webtool/public"), name="public")




@app.middleware("http")
async def disect_request(request: Request, call_next):
    logging.warning(f"TRACING: request {request.url} {request.headers=}")
    body = await request.body()
    logging.warning(f"TRACING: request body {body=}")
    response = await call_next(request)
    logging.warning(f"TRACING: response {response}, {type(response)=}")
    return response


@dataclass
class LoginData:
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
        version, status = apstra_server.apstra_server.login(login_data.host, login_data.port, login_data.username, login_data.password)
        logging.warning(f"login {status=} {version=}")
        return {"status": status, "version": version}
    except Exception as e:
        logging.error(f"login {e=}")
        return {"status": str(e), "version": ""}




# here we use our custom page decorator directly and just put the content creation into a separate function
@ui.page('/')
def index_page() -> None:
    with theme.frame('Homepage'):
        home_page.content()


# this call shows that you can also move the whole page creation into a separate file
all_pages.create()

ui.run_with(
    app,
    mount_path='/',
    title='Apstra Webtool',
)
