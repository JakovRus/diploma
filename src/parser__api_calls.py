import idaapi
import idautils
import idc

from parser__black_list import is_in_black_list


def get_start(address):
    return idaapi.get_func(int(address)).startEA


def get_end(address):
    return idaapi.get_func(int(address)).endEA


def get_function_address(head):
    return str(idc.get_operand_value(head, 0))


def find_addresses_for_mnem(addresses, address, mnem):
    for head in idautils.Heads(get_start(address), get_end(address)):
        name = idc.GetFunctionName(head)
        if idc.GetMnem(head) == mnem and not is_in_black_list(name):
            addresses.append(get_function_address(head))


def get_jmp_functions(address):
    addresses = []
    find_addresses_for_mnem(addresses, address, 'call')
    return addresses


def get_api_calls(address):
    calls = []
    for function in get_jmp_functions(address):
        if idc.get_segm_name(int(function)) == '.text':
            find_addresses_for_mnem(calls, function, 'jmp')

    return calls
