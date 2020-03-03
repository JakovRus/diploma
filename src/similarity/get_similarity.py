from src.k_gram.to_k_gram import k_gram_length
from src.utils.flatten import flatten


# p & q - k-grams
def get_similarity(p, q):
    if len(p) <= k_gram_length or len(q) <= k_gram_length:
        return 100 if len(get_intersection(flatten(p), flatten(q))) > 0 else 0

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

