def finder(arr1, arr2):
    for i in arr1:
        if i not in arr2:
            return i


def finder2(arr1, arr2):
    return sum(arr1) - sum(arr2)


def finder3(arr1, arr2):
    i = int()
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    while i < len(arr1):
        if arr1[i] != arr2[i]:
            return arr1[i]

        i += 1


def finder4(arr1, arr2):
    i = int()
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]


if __name__ == '__main__':
    print(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
    print(finder2([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
    print(finder3([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
    print(finder4([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
