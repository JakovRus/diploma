from src.k_gram.get_function_k_grams import get_function_k_grams
from src.code_parser.user_functions import get_user_functions
from get_similarity import get_similarity


def get_similar_functions(addr):
    similar_functions = []
    k_grams = get_function_k_grams(addr)
    user_functions = [func for func in get_user_functions() if func != addr]

    for func in user_functions:
        func_k_grams = get_function_k_grams(func)
        print(func_k_grams)
        similarity = get_similarity(k_grams, func_k_grams)

        if similarity > 50:
            similar_functions.append(func)

    return similar_functions

