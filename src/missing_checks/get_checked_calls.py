from src.function_parser.is_checked import is_checked
from src.utils.get_function_address import get_function_address


def get_checked_calls(calls_addresses):
    checked_calls = []

    for address in calls_addresses:
        if is_checked(address):
            checked_calls.append(get_function_address(address))

    return checked_calls
