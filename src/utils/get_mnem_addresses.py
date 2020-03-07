import idc
from function_addresses import get_function_heads
from list_to_hex import list_to_hex


def get_mnem_addresses(address, mnem_name):
    heads = get_function_heads(address)
    addresses = []

    for head in heads:
        mnem = idc.GetMnem(head)
        if mnem == mnem_name:
            addresses.append(head)

    return list_to_hex(addresses)

