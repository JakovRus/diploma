k_gram_length = 2


def to_k_gram(calls):
    k_grams = []

    if len(calls) <= k_gram_length:
        return [calls]

    for i in range(len(calls)):
        k_gram = calls[i:i + k_gram_length]

        if len(k_gram) == k_gram_length:
            k_grams.append(k_gram)

    return k_grams
