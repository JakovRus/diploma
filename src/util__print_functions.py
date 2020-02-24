import idc
from code_parser.functions_array import get_functions_array
from code_parser.user_functions import get_user_functions
from code_parser.api_calls import get_api_calls
from k_gram.to_k_gram import to_k_gram


def print_functions():
    idc.auto_wait()

    addresses = get_functions_array()

    f = open("output.txt", "w+")
    for address in addresses:
        f.write(idc.get_func_name(int(address)) + ':' + str(address) + "\n\n")

    f.close()


def print_user_functions():
    idc.auto_wait()

    addresses = get_user_functions()

    for address in addresses:
        print(idc.get_func_name(int(address)) + ':' + str(address) + "\n")
        calls = get_api_calls(address)
        print('k gramm: ')
        print(to_k_gram(calls))
        print('\n\n')
