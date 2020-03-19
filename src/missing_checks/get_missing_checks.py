from collections import Counter

from src.function_parser.get_calls_addresses import get_calls_addresses
from src.similarity.get_similar_functions import get_similar_functions
from src.utils.get_function_address import get_function_address
from src.utils.lists_diff import list_diff


def get_unchecked_calls(func_address, checked_calls):
    calls_addresses = get_calls_addresses(func_address)

    calls = []
    for address in calls_addresses:
        calls.append(get_function_address(address))

    return list_diff(calls, checked_calls[func_address])


def get_counted_checked_calls(checked_calls, similar_functions):
    counted_checked_calls = []
    for func in similar_functions:
        counted_checked_calls.extend(checked_calls[func])

    return Counter(counted_checked_calls)


def get_missing_checks(func_address, checked_calls):
    unchecked_calls = get_unchecked_calls(func_address, checked_calls)
    similar_functions = get_similar_functions(func_address)
    similar_functions_length = float(len(similar_functions))

    if not similar_functions_length:
        return []

    counted_checked_calls = get_counted_checked_calls(checked_calls, similar_functions)
    missing_checks = []

    for call in unchecked_calls:
        percentage = counted_checked_calls[call] / similar_functions_length
        if percentage >= 0.5:
            missing_checks.append(call)

    return missing_checks
