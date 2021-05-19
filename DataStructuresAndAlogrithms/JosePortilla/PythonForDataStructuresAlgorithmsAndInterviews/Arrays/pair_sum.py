def pair_sum(arr, s):
    pairs = set()

    for i in range(len(arr) - 1):
        if arr[i] + arr[i + 1] == s:
            pairs.add((arr[i], arr[i + 1]))

    return len(pairs)


if __name__ == '__main__':
    print(pair_sum([1, 3, 2, 2], 4))
