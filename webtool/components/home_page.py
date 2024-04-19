from nicegui import ui

from webtool.components import apstra_server
from webtool.components import generic_system

def content() -> None:
    apstra_server.content()

    ui.separator()

    generic_system.content()

    ui.separator()    
