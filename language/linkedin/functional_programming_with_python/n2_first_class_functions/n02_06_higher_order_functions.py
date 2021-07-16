def main():
    def divide(x, y):
        return x / y

    def second_argument_is_not_zero(func):
        def safe_version(*args):
            if not args[1]:
                print("Warning: second argument is zero")
                return
            return func(*args)

        return safe_version

    divide_safe = second_argument_is_not_zero(divide)
    divide_safe(10, 0)
    print(divide_safe(10, 2))


if __name__ == '__main__':
    main()
