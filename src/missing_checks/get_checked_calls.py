from src.function_parser.get_calls_addresses import get_calls_addresses
from src.function_parser.is_checked import is_checked
from src.utils.get_function_address import get_function_address


def get_checked_calls(address):
    calls_addresses = get_calls_addresses(address)
    checked_calls = []

    for address in calls_addresses:
        if is_checked(address):
            checked_calls.append(get_function_address(address))

    return checked_calls
