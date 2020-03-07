import idaapi
import idautils


def get_function_start(address):
    return idaapi.get_func(int(address)).startEA


def get_function_end(address):
    return idaapi.get_func(int(address)).endEA


def get_function_heads(address):
    return idautils.Heads(get_function_start(address), get_function_end(address))

