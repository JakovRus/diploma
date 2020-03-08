import idc
from code_parser.functions_array import get_functions_array
from code_parser.user_functions import get_user_functions
from get_checked_calls import get_checked_calls
from src.utils.get_function_address import get_function_address


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
        print('*******************')
        print(idc.get_func_name(int(address)) + ':' + str(address))
        print('------------------')
        calls = get_checked_calls(address)
        for call in calls:
            function_address = get_function_address(call)
            print(idc.get_func_name(int(function_address)) + ':' + str(function_address))

        print('*******************')

    # similar = get_similar_functions(addresses[0])
    #
    # print(idc.get_func_name(int(addresses[0])) + ':' + str(addresses[0]))
    # print('similar functions:')
    # for address in similar:
    #     print(idc.get_func_name(int(address)) + ':' + str(address))
    #     print('k gramm: ')
    #     print(get_function_k_grams(address))
