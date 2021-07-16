def main():
    numbers_list = [0, 1, 3, 4, 5, 6, 7, 8, 9]
    doubled_list = []
    for i in numbers_list:
        doubled_list.append(i * 2)
    print(doubled_list)

    def double(x):
        return x * 2

    doubled_list_functional = list(map(double, numbers_list))
    print(doubled_list_functional)


if __name__ == '__main__':
    main()
