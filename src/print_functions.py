import sys
import os
sys.path.append(os.getcwd())

import idc
from parser.user_functions import get_user_functions
from parser.api_calls import get_api_calls


def print_functions():
    idc.auto_wait()

    addresses = get_user_functions()

    f = open("output.txt", "w+")
    for address in addresses:
        print address
        f.write(idc.get_func_name(address) + ':' + str(address) + "\n")
        for call in get_api_calls(address):
            f.write(call)

    f.close()
    idc.Exit(0)
