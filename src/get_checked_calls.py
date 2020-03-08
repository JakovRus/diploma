from function_parser.get_calls_addresses import get_calls_addresses
from function_parser.is_checked import is_checked


def get_checked_calls(address):
    calls_addresses = get_calls_addresses(address)
    checked_calls = []

    for address in calls_addresses:
        if is_checked(address):
            checked_calls.append(address)

    return checked_calls
