from functools import reduce
from operator import mul


def is_prime(n):
    if n == 1:
        return True

    for i in range(2, n):
        if not n % i:
            return False

    return True


def get_prime_factors(n):
    if is_prime(n):
        return [n]

    primes = [p for p in range(2, n) if is_prime(p)]

    output = list()
    i = 0
    old_n = n
    while i < len(primes):
        prime = primes[i]

        while not n % prime:
            n /= prime
            output.append(prime)

        if reduce(mul, output, 1) == old_n:
            return output

        i += 1

    return list()


def get_prime_factors2(n):
    factors = list()
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1

    return factors


if __name__ == '__main__':
    for i in range(1, 100):
        print(i, get_prime_factors(i))

    for i in range(1, 100):
        print(i, get_prime_factors2(i))
