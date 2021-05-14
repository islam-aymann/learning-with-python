# define enumerations using the Enum base class

from enum import Enum, unique, auto, IntEnum


@unique  # avoid duplicate values
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()
    POTATO = "six"  # Enum supports other types along with int
    RICE = auto()


class Fruit2(Enum):
    APPLE, BANANA, ORANGE, TOMATO = [auto() for i in range(4)]


class Fruit3(IntEnum):  # Enum where members are also (and must be) ints
    APPLE, BANANA, ORANGE, TOMATO = [auto() for i in range(4)]


def main():
    # enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # print the auto-generated value
    print(Fruit.PEAR.value)

    # enums are hashable - can be used as keys
    my_fruits = dict()
    my_fruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(my_fruits[Fruit.BANANA])

    print(Fruit.POTATO.value)
    print(Fruit.RICE.value)

    print(Fruit2.BANANA.value)
    print(Fruit3.BANANA.value)


if __name__ == "__main__":
    main()
