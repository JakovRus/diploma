from src.k_gram.get_function_k_grams import get_function_k_grams
from src.code_parser.user_functions import get_user_functions
from get_similarity import get_similarity


def get_similar_functions(addr, calls_addresses):
    similar_functions = []
    k_grams = get_function_k_grams(addr, calls_addresses)

    for func in get_user_functions():
        if func == addr:
            continue

        func_k_grams = get_function_k_grams(func, calls_addresses)
        similarity = get_similarity(k_grams, func_k_grams)

        if similarity >= 50:
            similar_functions.append(func)

    return similar_functions

