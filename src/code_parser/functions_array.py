import idc
from user_functions import get_user_functions
from api_calls import get_api_calls


def get_functions_array():
    idc.auto_wait()

    addresses = get_user_functions()

    for address in addresses:
        calls = get_api_calls(address)
        addresses.extend(calls)

    return list(set(addresses))
