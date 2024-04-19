
from typing import Dict
from nicegui import ui, events
import logging
import pandas as pd
from io import StringIO


the_columns = [
    {"name": "blueprint", "label": "blueprint", "field": "blueprint"},
    {"name": "label", "label": "label", "field": "label"},
    {"name": "ae", "label": "ae", "field": "ae"},
    {"name": "cts", "label": "cts", "field": "cts"},
    {"name": "speed", "label": "speed", "field": "speed"},
    {"name": "tags", "label": "tags", "field": "tags"},
    {"name": "server_intf", "label": "server_intf", "field": "server_intf"},
    {"name": "switch", "label": "switch", "field": "switch"},
    {"name": "switch_intf", "label": "switch_intf", "field": "switch_intf"},
]

the_rows = []
the_ui_table = None
the_select_columns = None
the_df = None



def handle_csv_upload(e: events.UploadEventArguments) -> None:
    global the_columns, the_rows, the_ui_table, the_select_columns, the_df
    with StringIO(e.content.read().decode('utf-8')) as f:
        the_df = pd.read_csv(f) 

    ## verify the columns against the_columns
    columns=[{"name": col, "label": col, "field": col} for col in the_df.columns]
    pairs = zip(columns, the_columns)
    diffs = [(x, y) for x, y in pairs if x != y]
    if diffs:
        logging.error(f"handle_upload WRONG {diffs=}")

    # logging.warning(f"handle_upload {the_columns=}")
    the_rows=[{col: row[col] for col in the_df.columns} for _, row in the_df.iterrows()]
    the_ui_table = ui.table(columns=the_columns, rows=the_rows)

    # the_grouped = the_df.groupby('blueprint').apply(list).to_dict()
    the_grouped = {k: list(v) for k, v in the_df.groupby('blueprint')}
    logging.warning(f"handle_upload ######## groupdby: {the_grouped=}")


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
    with ui.row():
        ui.label('Generic System')
        ui.upload(on_upload=handle_csv_upload, label="csv upload", auto_upload=True).props('accept=.csv')
        ui.button('Clear Table', on_click=clear_table)
        ui.button('Download Sample', on_click=lambda: ui.download('/public/sample_generic_system.csv'))

