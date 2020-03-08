import idc

from black_list import is_in_black_list
from src.utils.function_addresses import get_function_heads
from src.utils.get_function_address import get_function_address


def find_addresses_for_mnem(addresses, address, mnem):
    for head in get_function_heads(address):
        is_mnem = idc.GetMnem(head) == mnem
        if not is_mnem:
            continue

        name = idc.GetFunctionName(int(get_function_address(head)))
        not_in_black_list = not is_in_black_list(name)
        if not_in_black_list:
            addresses.append(get_function_address(head))


def get_api_calls(address):
    if idc.get_segm_name(int(address)) != '.text':
        return []

    addresses = []
    find_addresses_for_mnem(addresses, address, 'call')
    return addresses
