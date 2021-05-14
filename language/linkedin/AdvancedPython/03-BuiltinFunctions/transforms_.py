# use transform functions like sorted, filter, map


def filter_func(x):
    if x % 2 == 0:
        return False
    return True


def filter_func2(x):
    if x.isupper():
        return False
    return True


def square_func(x):
    return x ** 2


def to_grade(x):
    if x >= 90:
        return "A"
    elif 80 <= x < 90:
        return "B"
    elif 70 <= x < 80:
        return "C"
    elif 65 <= x < 70:
        return "D"
    return "F"


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # use filter to remove items from a list
    odds = list(filter(filter_func, nums))
    print(odds)

    # you can use lambda expressions for simple functions
    evens = list(filter(lambda x: not x % 2, nums))
    print(evens)

    # use filter on non-numeric sequence
    lowers = list(filter(filter_func2, chars))
    print(lowers)

    # use map to create a new sequence of values
    squares = list(map(square_func, nums))
    print(squares)

    # use sorted and map to change numbers to grades
    grades = sorted(grades)
    letters = list(map(to_grade, grades))
    print(letters)


if __name__ == "__main__":
    main()
