import json
import logging
import asyncio
import ssl

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles

from webtool.components.socket import sio, socket_app
from webtool.components.apstra_server import apstra_server

logger = logging.getLogger('webtool.main')
app = FastAPI()

app.mount("/", socket_app)

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# ssl_context.load_cert_chain("certs/cert.pem", "certs/key.pem")

app.mount("/static", StaticFiles(directory="webtool/static"), name="static")
# app.mount("/js", StaticFiles(directory="webtool/static/js"), name="js")
# app.mount("/css", StaticFiles(directory="webtool/static/css"), name="css")
app.mount("/images", StaticFiles(directory="webtool/static/images"), name="images")


@sio.on('create-something')
async def create_something(sid, data):
    logger.warning(f"Client {sid} created something: {data}")
    await sio.emit('something-created', data)

@sio.on('msg')
async def handle_msg(sid, data):
    logger.warning(f"handle_msg({sid},{data})")
    await sio.emit('msg', data)

@sio.on('send_msg')
async def handle_send_msg(sid, data):
    logger.warning(f"handle_send_msg({sid}, {data})")
    await sio.emit('msg', data)


@app.get("/")

async def get_index_html():
    from webtool.pages import index_html
    return PlainTextResponse(index_html.content.strip('\n'), media_type="text/html")


@app.get("/css/style.css")
async def get_style_css():
    from webtool.pages import style_css
    return PlainTextResponse(style_css.content.strip('\n'), media_type="text/css")

@app.get("/js/main.js")
async def get_main_js():
    from webtool.pages import main_js
    return PlainTextResponse(main_js.content.strip('\n'), media_type="text/javascript")


def main():
    import sys
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    
    import uvicorn    
    uvicorn.run("webtool.main:app", host='0.0.0.0', port=8083, reload=True, log_level="info")

if __name__ == '__main__':
    main()