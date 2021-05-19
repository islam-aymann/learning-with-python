def uni_char(s):
    return len(set(s)) == len(s)


if __name__ == '__main__':
    print(uni_char('islamayman'))
