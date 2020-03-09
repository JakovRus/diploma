from collections import Counter
from src.function_parser.get_calls_addresses import get_calls_addresses
from src.missing_checks.get_checked_calls import get_checked_calls
from src.similarity.get_similar_functions import get_similar_functions
from src.utils.get_function_address import get_function_address
from src.utils.lists_diff import list_diff


def get_unchecked_calls(func_address):
    calls_addresses = get_calls_addresses(func_address)
    calls = []
    for address in calls_addresses:
        calls.append(get_function_address(address))

    checked_calls = get_checked_calls(func_address)
    return list_diff(calls, checked_calls)


def get_counted_checked_calls(func_address):
    similar_functions = get_similar_functions(func_address)

    checked_calls = []
    for func in similar_functions:
        checked_calls.extend(get_checked_calls(func))

    return Counter(checked_calls)


def get_missing_checks(func_address):
    unchecked_calls = get_unchecked_calls(func_address)
    similar_functions_length = len(get_similar_functions(func_address))

    if not similar_functions_length:
        return []

    checked_calls = get_counted_checked_calls(func_address)
    missing_checks = []

    for call in unchecked_calls:
        percentage = checked_calls[call] / similar_functions_length
        if percentage > 0.5:
            missing_checks.append(call)

    return missing_checks
