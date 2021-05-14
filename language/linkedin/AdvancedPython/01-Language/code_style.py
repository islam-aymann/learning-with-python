# imports go on their own lines
import os
import sys


# two blank lines separate classes from other functions
class MyClass(object):
    def __init__(self, prop2: int = None):
        self.prop1 = "my class"
        self._prop2 = prop2  # prop2 is internal class value

    @property
    def prop2(self):
        return self._prop2

    @prop2.setter
    def prop2(self, value: int):
        self._prop2 = value

    @prop2.deleter
    def prop2(self):
        del self._prop2

    # within classes, one blank line separates methods
    def method1(self, arg1):
        pass


def main():
    # Long comments, like this one that flow across several lines, are
    # limited to 72 characters instead of 79 for lines of code.
    cls1 = MyClass()
    cls1.prop1 = "hello world"

    print(os.getcwd())
    print(sys.getwindowsversion())


if __name__ == "__main__":
    main()
