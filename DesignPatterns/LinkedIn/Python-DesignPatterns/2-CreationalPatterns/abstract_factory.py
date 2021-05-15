class Dog:
    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """Returns a Dog object"""
        return Dog()

    def get_food(self):
        """Returns a Dog Food object"""
        return "Dog Food!"


class PetStore:
    """PetStore houses our abstract factory"""

    def __init__(self, pet_factory=None):
        """pet_factory is our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects returned by
        the DogFactory
        """

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"our pet is '{pet}'!.")
        print(f"Our pet says hello '{pet.speak()}'.")
        print(f"Its food is {pet_food}.")


if __name__ == '__main__':
    factory = DogFactory()
    shop = PetStore(pet_factory=factory)
    shop.show_pet()
