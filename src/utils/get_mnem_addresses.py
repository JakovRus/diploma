import idc
from function_addresses import get_function_heads
from list_to_int import list_to_int
from get_heads_to_address import get_heads_to_address


def find_mnems(heads, mnem_name):
    addresses = []

    for head in heads:
        mnem = idc.GetMnem(head)
        if mnem == mnem_name:
            addresses.append(head)

    return list_to_int(addresses)


def get_mnem_addresses(address, mnem_name):
    heads = get_function_heads(address)
    return find_mnems(heads, mnem_name)


def get_mnem_addresses_to_address(address, mnem_name):
    heads = get_heads_to_address(address)
    return find_mnems(heads, mnem_name)
