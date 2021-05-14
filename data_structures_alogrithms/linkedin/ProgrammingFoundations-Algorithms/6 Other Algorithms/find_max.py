def find_max(items):  # O(unordered list)
    if len(items) == 1:
        return items[0]

    op1 = items[0]
    print(op1)
    op2 = find_max(items[1:])
    print(op2)

    return op1 if op1 > op2 else op2


if __name__ == '__main__':
    items1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print(find_max(items1))
