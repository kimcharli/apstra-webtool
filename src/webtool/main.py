from reactpy import component, html
from reactpy.backend.fastapi import configure, Options
from fastapi import FastAPI, Request, UploadFile, Form
import logging
import os


@component
def HelloWorld():
    return html.h1("Hello, world!")

The_Title = os.environ.get('WEB_TITLE', "Apstra Webtool")
# The_Title = "Apstra Webtool"
options = Options
the_title = [x for x in options.head if x['tagName'] == 'title']
the_title[0]['children'] = [The_Title]

# logging.error(f"after {options.head=}")

app = FastAPI()
configure(app, HelloWorld)
