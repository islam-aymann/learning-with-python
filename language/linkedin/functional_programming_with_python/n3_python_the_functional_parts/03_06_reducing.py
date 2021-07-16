from functools import reduce


def main():
    numbers_list = [0, 1, 3, 4, 5, 6, 7, 8, 9]

    def get_sum(acc, x):
        print(f"acc is {acc} and x is {x}")
        return acc + x

    summing1 = reduce(get_sum, numbers_list)
    print(summing1)

    summing2 = reduce(lambda acc, x: acc + x, numbers_list)
    print(summing2)


if __name__ == '__main__':
    main()
