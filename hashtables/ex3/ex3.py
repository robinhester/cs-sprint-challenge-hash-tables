# pass

def intersection(arrays):
    """
    YOUR CODE HERE
    """

    counts = {}
    result = []

    for array in arrays:
        for i in array:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1

    for i in counts:
        if counts[i] >1:
            result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
