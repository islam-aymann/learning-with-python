def power(num: int, pwr: int) -> int:
    if not pwr:
        return 1
    return num * power(num, pwr-1)


def factorial(num: int) -> int:
    if not num:
        return 1
    return num * factorial(num - 1)


if __name__ == '__main__':
    print(f"5 to the power of 3 is {power(5, 3)}")
    print(f"1 to the power of 5 is {power(1, 5)}")
    print(f"4! is {factorial(4)}")
    print(f"0! is {factorial(0)}")
