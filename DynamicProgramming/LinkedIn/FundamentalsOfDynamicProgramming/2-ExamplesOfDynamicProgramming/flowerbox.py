def flowerbox(nutrient_values):
    a = 0  # f(i-2)
    b = 0  # f(i-1)

    for val in nutrient_values:
        a, b = b, max(a + val, b)

    return b


if __name__ == '__main__':
    l1 = [3, 10, 2, 1, 2]
    l2 = [9, 10, 9]
    print(f"flowerbox({l1}) = {flowerbox(l1)}")
    print(f"flowerbox({l2}) = {flowerbox(l2)}")
