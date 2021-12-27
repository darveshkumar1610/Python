# Test Class

class Person:
    # Weak Private, Do not rely on _name variable, instead we should use functions to get and set values.
    _name = 'No Name'

    def setName(self, name):
        self._name = name
        print(f'Name set to {self._name}')

    # Strong Private (Double underscore)
    def __think(self):
        print('Thinking to myself')

    def work(self):
        self.__think()

    # Before and After
    def __init__(self):                         # Automatically run at each time.
        print('Constructor for each class')
    def __call__(self):                         # We should not use like this. Instead use Getter & Setter.
        print('Call for someone')

class Child(Person):
    def testDouble(self):
        self.__think(self)