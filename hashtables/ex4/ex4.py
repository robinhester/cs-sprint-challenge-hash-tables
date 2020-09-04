# pass

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    hash_table = {}

    for i in a:
        if i not in hash_table:
            hash_table[i] = i*-1
            if hash_table[i] in hash_table and i != 0:
                result.append(abs(hash_table[i]))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
