import timeit


def fib(n: int):
    a = 1  # fib(i-2)
    b = 1  # fib(i-1)

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


if __name__ == '__main__':
    values = range(10, 1000, 10)

    for value in values:
        print(f"for {value}:",
              timeit.timeit(f"fib({value})", number=100, globals=globals()))
