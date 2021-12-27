# Exception: Bad things usually happens, how to handle them

"""
Errors mostly occur at runtime that's they belong to an UNCHECKED Type.
Exceptions are the problems which can occur at compile time or runtime.
Exceptions mainly occurs in the code written by developers.
Divided into 2-categories: Checked (compile) and Unchecked (runtime)
More details on https://docs.python.org/3/library/exceptions.html
"""


# Simple Decorator
def outline(func):
    def inner(*args, **kwargs):
        print('-' * 20)
        print(f'Function: {func.__name__}')
        func(*args, **kwargs)
        print('-' * 20)

    return inner


# Try, Except and Finally
@outline
def testing(x, y):
    try:
        # Attempt
        z = x / y
        print(f'Result: {z}')
    except:
        # catch in other languages
        print(f'Something bad happened x:{x} y:{y}')
    finally:
        # Going to run anyhow, no matter what ever happens
        print('Complete')

testing(5,0)
testing(5,'cat')
testing(5,2)

