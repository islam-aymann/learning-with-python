def permutations(lst: list):
    if len(lst) == 0:
        return list()

    if len(lst) == 1:
        return [lst]

    new_lst = list()

    for i in range(len(lst)):
        m = lst[i]
        rem = lst[:i] + lst[i + 1 :]

        for p in permutations(rem):
            new_lst.append([m] + p)

    return new_lst


if __name__ == "__main__":
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input()
    x = 2
    y = 2
    z = 2
    n = 2

    lst = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]
    print(lst)
