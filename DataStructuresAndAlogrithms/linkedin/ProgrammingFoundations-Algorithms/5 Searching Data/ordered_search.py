def binary_search(item, items_list):
    size = len(items_list) - 1
    lower_idx = 0
    upper_idx = size

    while lower_idx <= upper_idx:
        mid_point = (lower_idx + upper_idx) // 2

        if items_list[mid_point] == item:
            return mid_point

        if item > items_list[mid_point]:
            lower_idx = mid_point + 1

        else:
            upper_idx = mid_point - 1


if __name__ == '__main__':
    items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

    print(binary_search(6, items))
    print(binary_search(87, items))
    print(binary_search(250, items))
