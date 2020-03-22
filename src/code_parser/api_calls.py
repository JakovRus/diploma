from src.utils.get_function_address import get_function_address


def get_api_calls(calls_addresses):
    return [get_function_address(call) for call in calls_addresses]
