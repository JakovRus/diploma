import re
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

    return addresses


def filter_invalid_names(addresses):
    valid_addresses = []
    for address in addresses:
        name = GetFunctionName(address)

        if re.match(r'[A-Za-z_]', name[0]):
            valid_addresses.append(address)

    return valid_addresses


def get_demangled_name(address):
    return Demangle(get_func_name(address), GetLongPrm(idc.INF_LONG_DN))


def is_valid_name(address):
    name = Demangle(get_func_name(address), GetLongPrm(idc.INF_LONG_DN))
    print name
    # return name is not None & not not re.match(r'[A-Za-z_]', name[0])
    return True


def is_user_function(address):
    name = GetFunctionName(address)

    is_valid = is_valid_name(address)
    not_in_black_list = not is_in_black_list(name)

    return is_valid & not_in_black_list
