from idaapi import *
from idautils import *
from idc import *


def get_user_functions():
    addresses = []

    for function in Functions():
        flags = GetFunctionFlags(function)
        if flags & FUNC_LIB or flags & FUNC_THUNK:
            continue

        if SegName(function) != '.text':
            continue

        addresses.append(function)

    return addresses
