import idaapi
from src.utils.list_to_hex import list_to_hex


def get_args(call):
    return list_to_hex(idaapi.get_arg_addrs(call))
