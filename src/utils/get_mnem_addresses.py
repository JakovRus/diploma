import idc
from function_addresses import get_function_heads
from get_heads_to_address import get_heads_to_address


def find_mnems(heads, mnem_name):
    return list(filter(lambda head: idc.GetMnem(head) == mnem_name, heads))


def get_mnem_addresses(address, mnem_name):
    heads = get_function_heads(address)
    return find_mnems(heads, mnem_name)


def get_mnem_addresses_to_address(address, mnem_name):
    heads = get_heads_to_address(address)
    return find_mnems(heads, mnem_name)
