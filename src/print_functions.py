import idc
import functions_utils


def print_functions():
    idc.auto_wait()

    addresses = functions_utils.get_user_functions()

    f = open("output.txt", "w+")
    for address in addresses:
        print f.write(idc.get_func_name(address) + "\n")

    f.close()
    idc.Exit(0)
