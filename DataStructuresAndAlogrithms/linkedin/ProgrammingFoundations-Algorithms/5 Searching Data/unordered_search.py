def find_item(item, items_list):
    for i, val in enumerate(items_list):
        if val == item:
            return item


if __name__ == '__main__':
    items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

    print(find_item(87, items))
    print(find_item(250, items))
