from idaapi import *
from idautils import *
from idc import *
from black_list import *


def get_user_functions():
    addresses = []

    for function in Functions():
        flags = GetFunctionFlags(function)
        if flags & FUNC_LIB or flags & FUNC_THUNK:
            continue
        addresses.append(function)

    addresses = filter_invalid_names(addresses)
    return addresses


def filter_invalid_names(addresses):
    valid_addresses = []
    for address in addresses:
        if is_user_function(address):
            valid_addresses.append(address)

    return valid_addresses


def is_user_function(address):
    name = GetFunctionName(address)

    matches_pattern = re.match(r'\?[A-Za-z_][A-Za-z_0-9@]*@@[A-Z@]*', name)
    not_in_black_list = not is_in_black_list(name)

    return matches_pattern and not_in_black_list
