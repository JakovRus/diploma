import idc
from src.utils.get_mnem_addresses import get_mnem_addresses


def get_calls_addresses(address):
    if idc.get_segm_name(int(address)) != '.text':
        return []

    return get_mnem_addresses(address, 'call')
