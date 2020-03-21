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


def get_using_functions(similar_functions, checked_calls, call):
    return list(filter(lambda func: call in checked_calls[func], similar_functions))


def get_missing_checks(func_address, checked_calls):
    unchecked_calls = get_unchecked_calls(func_address, checked_calls)
    similar_functions = get_similar_functions(func_address)

    if not len(similar_functions):
        return []

    counted_checked_calls = get_counted_checked_calls(checked_calls, similar_functions)
    missing_checks = []

    for call in unchecked_calls:
        using_functions = get_using_functions(similar_functions, checked_calls, call)
        length = float(len(using_functions))
        percentage = counted_checked_calls[call] / length if length else 0

        if percentage >= 0.5:
            missing_checks.append(call)

    return missing_checks
