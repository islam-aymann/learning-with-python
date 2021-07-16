import math


def main():
    def double(x):
        return x * 2

    def minus_one(x):
        return x - 1

    def squared(x):
        return x * x

    function_list = [
        double,
        minus_one,
        squared,
        math.sqrt
    ]

    my_number = 3

    for func in function_list:
        my_number = func(my_number)

    print(my_number)


if __name__ == '__main__':
    main()
