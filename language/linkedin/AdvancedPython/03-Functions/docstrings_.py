# Demonstrate the use of function docstrings

def my_function(arg1: int, arg2: str = None) -> None:
    """my_function(arg1: int, arg2: str = None) -> None --> Doesn't really
    do anything special.

    :param arg1: the first argument. Whatever you feel like passing.
    :param arg2: the second argument. Defaults to None.
        Whatever makes you happy.
    :return: nothing special only None, this line should be omitted as
        the function returns None
    :
    """
    print(arg1, arg2)


def main():
    print(my_function.__doc__)


if __name__ == "__main__":
    main()
