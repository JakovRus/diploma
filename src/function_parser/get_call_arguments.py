import idc

from get_args_addresses import get_args_addresses


def get_opnd(address):
    opnd = idc.GetOpnd(address, 1)

    if opnd == '':
        opnd = idc.GetOpnd(address, 0)

    return opnd


def get_call_arguments(call):
    addresses = get_args_addresses(call)
    arguments = []

    for address in addresses:
        opnd = get_opnd(address)
        arguments.append(opnd)

    return arguments
