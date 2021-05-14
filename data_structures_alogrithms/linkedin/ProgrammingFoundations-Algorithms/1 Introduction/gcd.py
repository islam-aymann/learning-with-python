def gcd(a: int, b: int) -> int:

    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b


if __name__ == '__main__':
    print(gcd(60, 96))
