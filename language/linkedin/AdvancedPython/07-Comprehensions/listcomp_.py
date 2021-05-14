# Demonstrate how to use list comprehensions


def main():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # Perform a mapping and filter function on a list
    even_squared = list(
        map(lambda e: e ** 2, filter(lambda e: 4 < e < 16, evens)))
    print(even_squared)

    # Derive a new list of numbers frm a given list
    even_squared = [e ** 2 for e in evens]
    print(even_squared)

    # Limit the items operated on with a predicate condition
    odd_squared = [e ** 2 for e in odds if 3 < e < 17]
    print(odd_squared)

    # You can have multiple nested for loops
    lst = [
        [i, j, k]
        for i in range(1)
        for j in range(2)
        for k in range(3)
        if i + j + k != 5
    ]

    print(lst)


if __name__ == "__main__":
    main()
