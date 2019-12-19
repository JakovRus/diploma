import idaapi
import idautils
import idc

from black_list import is_in_black_list


def get_start(address):
    return idaapi.get_func(int(address)).startEA


def get_end(address):
    return idaapi.get_func(int(address)).endEA


def get_function_address(head):
    return str(idc.get_operand_value(head, 0))


def find_addresses_for_mnem(addresses, address, mnem):
    for head in idautils.Heads(get_start(address), get_end(address)):
        is_mnem = idc.GetMnem(head) == mnem
        if not is_mnem:
            continue

        name = idc.GetFunctionName(int(get_function_address(head)))
        not_in_black_list = not is_in_black_list(name)
        if not_in_black_list:
            addresses.append(get_function_address(head))


def get_api_calls(address):
    addresses = []
    find_addresses_for_mnem(addresses, address, 'call')
    return addresses
