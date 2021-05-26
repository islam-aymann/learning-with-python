import re


def is_palindrome(ph):
    pnc = [" ", ",", ".", "-"]
    for pn in pnc:
        ph = ph.lower().replace(pn, '')

    hp = ''.join(ph[::-1])
    return hp == ph


def is_palindrome2(ph):
    forwards = ''.join(re.findall(r'[a-z]', ph.lower()))
    return forwards == forwards[::-1]


def is_palindrome3(ph: str):
    forwards = ''.join(p for p in ph if p.isalpha())
    return forwards == forwards[::-1]


if __name__ == '__main__':
    phrases = ["hello world", "level", "race car", "abc--33--cba"]
    for phrase in phrases:
        print(is_palindrome3(phrase))
