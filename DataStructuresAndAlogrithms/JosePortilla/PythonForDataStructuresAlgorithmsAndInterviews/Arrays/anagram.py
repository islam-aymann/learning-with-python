def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    s3 = s2[:]

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in s3:
            s3 = s3.replace(i, '', 1)

    if not s3:
        return True

    return False


def anagram2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)


def anagram3(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    d1 = dict()
    d2 = dict()
    for char in s1:
        d1[char] = d1.get(char, 0) + 1

    for char in s2:
        d2[char] = d2.get(char, 0) + 1

    return d1 == d2


if __name__ == '__main__':
    print(anagram('clint eastwood', 'old west action'))
    print(anagram('aa', 'bb'))

    print(anagram2('clint eastwood', 'old west action'))
    print(anagram2('aa', 'bb'))

    print(anagram3('clint eastwood', 'old west action'))
    print(anagram3('aa', 'bb'))
