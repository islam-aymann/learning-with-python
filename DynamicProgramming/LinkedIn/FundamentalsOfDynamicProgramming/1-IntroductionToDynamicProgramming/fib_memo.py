import timeit


def fib(n: int, cache=None):
    if not n or n == 1:
        return 1

    if cache is None:  # if not cache is invalid
        cache = dict()

    if n in cache:
        return cache[n]

    result = fib(n - 1, cache) + fib(n - 2, cache)
    cache[n] = result
    return result


if __name__ == '__main__':
    values = range(10, 1000, 10)

    for value in values:
        print(f"for {value}:",
              timeit.timeit(f"fib({value})", number=100, globals=globals()))
