import logging
from webtool.components.socket import sio, SocketEnum

logger = logging.getLogger('generic_system')

sample_gs_csv = """blueprint,server_label,is_external,server_tags,link_group_ifname,link_group_lag_mode,link_group_ct_names,link_group_tags,link_speed,server_ifname,switch_label,switch_ifname,link_tags,comment
terra,single-home-1,,single,,,vn20,single,10g,eth0,server_1,xe-0/0/11,,
terra,dual-home-1,,dual,ae101,lacp_active,"vn20,vn101",dual,10g,eth0,server_1,xe-0/0/12,forceup,
terra,dual-home-1,,dual,ae101,lacp_active,"vn20,vn101",dual,10g,eth1,server_2,xe-0/0/12,,
"""

@sio.on(SocketEnum.GS_SAMPLE)
async def generic_system_sample(sid, data):
    logger.warning(f"generic_system_sample begin: {sid}")
    await sio.emit(SocketEnum.GS_SAMPLE, {'file_content': sample_gs_csv})    
    logger.warning(f"generic_system_sample end: {sid} connected")

generic_system = None