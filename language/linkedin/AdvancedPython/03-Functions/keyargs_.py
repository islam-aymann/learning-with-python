# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def my_function(arg1, arg2, *, suppress_exceptions=False):
    print(arg1, arg2, suppress_exceptions)


def main():
    # try to call the function without the keyword
    # my_function(1, 2, True)
    my_function(1, 2, suppress_exceptions=True)


if __name__ == "__main__":
    main()
