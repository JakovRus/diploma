from function_addresses import get_function_start
import idautils


def get_heads_to_address(address):
    start = get_function_start(address)
    return reversed(list(idautils.Heads(start, int(address))))
