# In Python, Everything is an Object means functions can be used as Objects
# A Decorator takes in a function, adds some functionality and returns it.

# Basic decorator, Change the execution order
def test_decorator(func):               # It is not returning anything
    print('before')
    func()
    print('after')


@test_decorator                         # But create decorator like this, above a function.
def do_something():                     # This function will be used in above func() and returns output.
    print('Doing Something')


# f = test_decorator(do_something)       # Decorator usage

# Real Decorator, Change the functionality
def makeBold(func):
    def inner():
        print('<b>')
        func()
        print('</b>')

    return inner                          # Return the inner function


@makeBold
def printName():
    print('Darvesh Kumar')


printName()  # Run the inner function i.e. inner() and give the output of that.


# Decorators with defined no. of Parameters for both inner and divide function
def numcheck(func):
    def checkInt(o):
        if isinstance(o, int):
            if o == 0:
                print('Can not divide by zero')
                return False()
            return True
        print(f'{o} is not a number')
        return False

    def inner(x, y):
        if not checkInt(x) or not checkInt(y):
            return
        return func(x, y)

    return inner


@numcheck
def divide(a, b):
    print(a / b)


divide(100, 3)


# divide(100, 0)
# divide(100, 'cat')


# Decorator with unknown number of parameters. A decorator that can pass params and handle anything
# We also want to chain them together. *args, **kwargs to the rescue
def outline(func):
    def inner(*args, **kwargs):
        print('~' * 20)
        func(*args, **kwargs)
        print('+' * 20)

    return inner


def list_items(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(f'args = {args}')
        print(f'kwargs = {kwargs}')
        for x in args:
            print(f'args={x}')
        for k, v in kwargs.items():
            print(f'key={k}, value={v}')


@outline
@list_items
def display(msg):
    print(msg)


display('hello world')
