def to_k_gram(calls):
    length = 2
    k_grams = []

    if len(calls) <= length:
        return [calls]

    for i in range(len(calls)):
        k_gram = calls[i:i + length]

        if len(k_gram) == length:
            k_grams.append(k_gram)

    return k_grams
