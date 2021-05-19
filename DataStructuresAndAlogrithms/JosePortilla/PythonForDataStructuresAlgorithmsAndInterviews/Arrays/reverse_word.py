def rev_word(s):
    s = s.strip()
    s_lst = s.split(' ')
    n_lst = list()
    for i in range(len(s_lst)):
        n_lst.append(s_lst.pop())
    return n_lst


if __name__ == '__main__':
    print(rev_word(' space before'))
