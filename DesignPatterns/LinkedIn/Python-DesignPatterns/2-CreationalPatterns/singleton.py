class Borg:
    """Borg class making class attributes global"""
    _shared_state = dict()

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):
    """This class now shares all its attributes among various instances"""

    # This essentially makes the singleton object an object-oriented global
    # variable

    def __init__(self, **kwargs):
        # Borg.__init__(self)
        super(Singleton, self).__init__()
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)


if __name__ == '__main__':
    x = Singleton(HTTP="Hyper Text Transfer Protocol")
    print(x)

    y = Singleton(SNMP="Simple Network Management Protocol")
    print(y.HTTP)
    print(y.SNMP)
