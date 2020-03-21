import idc

from src.function_parser.get_calls_addresses import get_calls_addresses
from src.utils.get_function_address import get_function_address


def get_api_calls(address):
    if idc.get_segm_name(int(address)) != '.text':
        return []

    return [get_function_address(call) for call in get_calls_addresses(address)]
