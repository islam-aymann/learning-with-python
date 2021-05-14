import timeit


def fib(n: int):
    if not n or n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    values = [10, 20, 30]

    for value in values:
        print(f"for {value}:",
              timeit.timeit(f"fib({value})", number=100, globals=globals()))
