class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow"


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof"


def get_pet(pet="dog"):
    """the factory method"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]


if __name__ == '__main__':
    d = get_pet("dog")
    print(d.speak())

    c = get_pet("cat")
    print(c.speak())
