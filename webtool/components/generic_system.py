
from typing import Dict
from nicegui import ui, events
import logging
import pandas as pd
import numpy as np
from io import StringIO

from ck_apstra_api import generic_system
from webtool.components.apstra_server import apstra_server


the_columns = [
    {"name": "blueprint", "label": "blueprint", "field": "blueprint"},
    {"name": "system_label", "label": "system_label", "field": "system_label"},
    {"name": "is_external", "label": "is_external", "field": "is_external"},

    {"name": "speed", "label": "speed", "field": "speed"},
    {"name": "lag_mode", "label": "lag_mode", "field": "lag_mode"},
    {"name": "ct_names", "label": "ct_names", "field": "ct_names"},
    {"name": "gs_tags", "label": "gs_tags", "field": "gs_tags"},

    {"name": "server_intf1", "label": "server_intf1", "field": "server_intf1"},
    {"name": "switch1", "label": "switch1", "field": "switch1"},
    {"name": "switch_intf1", "label": "switch_intf1", "field": "switch_intf1"},

    {"name": "server_intf2", "label": "server_intf2", "field": "server_intf2"},
    {"name": "switch2", "label": "switch2", "field": "switch2"},
    {"name": "switch_intf2", "label": "switch_intf2", "field": "switch_intf2"},

    {"name": "server_intf3", "label": "server_intf3", "field": "server_intf3"},
    {"name": "switch3", "label": "switch3", "field": "switch3"},
    {"name": "switch_intf3", "label": "switch_intf3", "field": "switch_intf3"},

    {"name": "server_intf4", "label": "server_intf4", "field": "server_intf4"},
    {"name": "switch4", "label": "switch4", "field": "switch4"},
    {"name": "switch_intf4", "label": "switch_intf4", "field": "switch_intf4"},

    {"name": "comment", "label": "comment", "field": "comment"},

]

the_rows = []
the_ui_table = None
the_select_columns = None
the_df = None



def handle_csv_upload(e: events.UploadEventArguments) -> None:
    global the_columns, the_rows, the_ui_table, the_select_columns, the_df
    with StringIO(e.content.read().decode('utf-8')) as f:
        # should replace NaN with None
        the_df = pd.read_csv(f).replace(np.nan, None)

    ## verify the columns against the_columns
    columns=[{"name": col, "label": col, "field": col} for col in the_df.columns]
    pairs = zip(columns, the_columns)
    diffs = [(x, y) for x, y in pairs if x != y]
    if diffs:
        logging.error(f"handle_upload WRONG {diffs=}")

    # logging.warning(f"handle_upload {the_columns=}")
    the_rows=[{col: row[col] for col in the_df.columns} for _, row in the_df.iterrows()]
    the_ui_table = ui.table(columns=the_columns, rows=the_rows).props("square outlined")

    # the_grouped = the_df.groupby('blueprint').apply(list).to_dict()
    the_grouped = {k: list(v) for k, v in the_df.groupby('blueprint')}
    logging.warning(f"handle_upload ######## groupdby: {the_grouped=}")


    # def toggle(column: Dict, visible: bool) -> None:
    #     column['classes'] = '' if visible else 'hidden'
    #     column['headerClasses'] = '' if visible else 'hidden'
    #     the_table.update()

    # with ui.button('Columns', icon='menu'):
    #     with ui.menu(), ui.column().classes('gap-0 p-2'):
    #         for column in the_columns:
    #             ui.switch(column['label'], value=True, on_change=lambda e,
    #                     column=column: toggle(column, e.value))

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


def deploy() -> None:
    global the_df
    all_gs_spec = {}
    for bp_label in [x for x in the_df.groupby('blueprint').groups.keys()]:
        bp_spec = all_gs_spec[bp_label] = {}
        for gs_label in [x for x in the_df[the_df['blueprint'] == bp_label].groupby('system_label').groups.keys()]:
            # bp_spec[gs_label] = [x for x in the_df[(the_df['blueprint'] == bp_label) & (the_df['system_label'] == gs_label)]]
            bp_spec[gs_label] = the_df[(the_df['blueprint'] == bp_label) & (the_df['system_label'] == gs_label)].to_dict('records')
    logging.warning(f"deploy {all_gs_spec=}")
    _, error = generic_system.add_generic_system(apstra_server.apstra_server, all_gs_spec)
    if error:
        logging.error(f"deploy {error=}")    
 

def content() -> None:
    global the_columns
    with ui.row().classes('w-full items-left gap-0'):
        # ui.label('Generic System').classes('text-2xl font-bold')
        ui.button('Deploy Generic System', on_click=deploy)
        ui.button('Download Sample', on_click=lambda: ui.download('/public/sample_generic_system.csv'))
    with ui.row().classes('w-full items-left gap-0'):
        ui.upload(on_upload=handle_csv_upload, label="csv upload", auto_upload=True).props('accept=.csv')
        ui.button('Clear Table', on_click=clear_table)

