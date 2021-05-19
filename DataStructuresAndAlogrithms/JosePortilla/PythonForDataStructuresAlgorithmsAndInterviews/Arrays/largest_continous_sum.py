def large_con_sum(arr):
    s = 0
    m = 0
    for n in arr:
        s = max(s+n, n)
        m = max(m, s)

    return m


if __name__ == '__main__':
    ls = large_con_sum([1, 2, -1, 3, 4, -1])
    print(ls)

    ls = large_con_sum([1, 2, -1, 3, 4, 10, 10, -10, -1])
    print(ls)

    ls = large_con_sum([-1, 1])
    print(ls)
