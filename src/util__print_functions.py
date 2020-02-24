import idc
from code_parser.functions_array import get_functions_array


def print_functions():
    idc.auto_wait()

    addresses = get_functions_array()

    f = open("output.txt", "w+")
    for address in addresses:
        f.write(idc.get_func_name(int(address)) + ':' + str(address) + "\n\n")
    # f.write(str(len(addresses)))

    f.close()
