from src.k_gram.to_k_gram import k_gram_length
from src.utils.flatten import flatten


def k_gram_to_list(k_gram):
    return [str(item) for item in flatten(k_gram)]


# p & q - k-grams
def get_similarity(p, q):
    if len(p) <= k_gram_length or len(q) <= k_gram_length:
        intersection = get_intersection(k_gram_to_list(p), k_gram_to_list(q))
    else:
        intersection = get_intersection(p, q)

    p_to_q = (float(len(intersection)) / len(p))
    q_to_p = (float(len(intersection)) / len(q))

    return min(p_to_q, q_to_p) * 100


def get_separator():
    return '___'


def list_to_string(_list):
    separator = get_separator()
    return separator.join(str(item) for item in _list)


def k_grams_to_string(k_grams):
    list_of_strings = []

    for k_gram in k_grams:
        list_of_strings.append(list_to_string(k_gram))

    return list_of_strings


def string_to_array(_str):
    separator = get_separator()

    if not _str:
        return []

    split = _str.split(separator)

    return [int(item) for item in split]


def get_intersection(p, q):
    string_p = k_grams_to_string(p)
    string_q = k_grams_to_string(q)

    intersection = []
    string_intersection = list(set(string_p) & set(string_q))

    for string_k_gram in string_intersection:
        intersection.append(string_to_array(string_k_gram))

    return intersection
