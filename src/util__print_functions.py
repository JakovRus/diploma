import idc
from parser__user_functions import get_user_functions
from parser__api_calls import get_api_calls


def print_functions():
    idc.auto_wait()

    addresses = get_user_functions()

    f = open("output.txt", "w+")
    for address in addresses:
        f.write(idc.get_func_name(address) + ':' + str(address) + "\n")
        for call in get_api_calls(address):
            f.write(idc.get_func_name(int(call)) + ':' + str(call) + "\n")
        f.write("\n\n")

    f.close()
