def main():
    list1 = [1, 2, 3, 0, 5, 6]
    list2 = [1, 2, 3, 4, 5, 6]
    list3 = ["one", 2, 3, 4, 5, 6]

    # any() returns True if any of the sequence values evaluates to True
    print(any(list1))
    print(any(list2))
    print(any(list3))

    # all() returns True if all of the sequence values evaluates to True
    print(all(list1))
    print(all(list2))
    print(all(list3))

    # min() returns The minimum value of the sequence values
    print(min(list1))
    print(min(list2))

    # max() returns The maximum value of the sequence values
    print(max(list1))
    print(max(list2))

    try:
        print(min(list3))
        print(max(list3))
    except TypeError:
        pass
        # '<' not supported between instances of 'int' and 'str'


if __name__ == '__main__':
    main()
