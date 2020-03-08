import idaapi
from src.utils.list_to_int import list_to_int


def get_args_addresses(call):
    return list_to_int(idaapi.get_arg_addrs(call))
