def main():
    numbers_list = [0, 1, 3, 4, 5, 6, 7, 8, 9]
    even_numbers = []
    for x in numbers_list:
        if x % 2 == 0:
            even_numbers.append(x)

    print(even_numbers)

    def is_even(x):
        return not x % 2

    even_numbers_functional = list(filter(is_even, numbers_list))
    print(even_numbers_functional)


if __name__ == '__main__':
    main()
