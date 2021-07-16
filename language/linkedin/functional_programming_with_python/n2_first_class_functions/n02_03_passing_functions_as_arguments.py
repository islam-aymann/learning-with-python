def main():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def combine_2_and_3(func):
        return func(2, 3)

    print(combine_2_and_3(subtract))

    def combine_names(func):
        return func("Islam", "Ayman")

    def append_with_space(str1, str2):
        return f"{str1} {str2}"

    print(combine_names(append_with_space))

    def get_government_form_notation(first, last):
        return f"{last.upper()}, {first.upper()}"

    print(combine_names(get_government_form_notation))


if __name__ == '__main__':
    main()
