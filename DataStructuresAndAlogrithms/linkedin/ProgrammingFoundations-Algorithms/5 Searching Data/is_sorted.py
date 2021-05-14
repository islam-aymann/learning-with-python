def is_sorted1(item_list):
    for i in range(len(item_list) - 1):
        if item_list[i] > item_list[i + 1]:
            return False
    return True


def is_sorted2(item_list):
    return all([item_list[i] <= item_list[i + 1] for i in range(len(item_list) - 1)])


def main():
    items1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    items2 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

    print(is_sorted1(items1))
    print(is_sorted1(items2))

    print(is_sorted2(items1))
    print(is_sorted2(items2))


if __name__ == '__main__':
    main()
