def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    hash_table = {}

    for i in range(length):
        if weights[i] in hash_table.keys():
            hash_table[weights[i]] = [hash_table[weights[i]], i]
        else:
            hash_table[weights[i]] = i

        weight_remaining = limit - weights[i]
        if weight_remaining == weights[i]:
            if isinstance(hash_table[weight_remaining], list):
                indices = sorted(hash_table[weight_remaining], reverse=True)
                return indices
            else:
                continue
        
        if weight_remaining in hash_table.keys():
            weights = [weight_remaining, weights[i]]
            indices = sorted([hash_table[weight] for weight in weights], reverse=True)
            return indices

    return None

weight = [8, 8]

answer = get_indices_of_item_weights(weight, 2, 8)

