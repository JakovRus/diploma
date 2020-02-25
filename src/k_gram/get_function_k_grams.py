from src.code_parser.api_calls import get_api_calls
from to_k_gram import to_k_gram


def get_function_k_grams(addr):
    calls = get_api_calls(addr)
    return to_k_gram(calls)

