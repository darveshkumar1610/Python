# The underscore, often ignored but having multiple uses
# _Single (weak private) for Internal use Only within Class.
# __Double (Internal Use Only), avoid conflict in subclass and tell python to rewrite the name(Mangling)
# __Before
# After__ (Helps to avoid naming conflicts with reserved keywords like class)
# __Both__

# Skipping the Variable
for _ in range(5):
    print('hello')

### Test Class
from person import *                # File name (without .py extension) is the module name.

### Single
p = Person()
p.setName('Darvesh')
print(f'Weak Private {p._name}')

p._name = "Do not use this"
print(f'Weak Private {p._name}')

### Double
p = Person()
p.work()                    # It can fetch work function from Person class

# p.__think()
# c = Child()
# c.testDouble()

### After (Any no. of underscores)
#class = Person()                # It will give invalid syntax
class_ = Person()                # It will work
print(class_)

### Before and After : considered Special to Python, like 'init' and 'main' function
p = Person()
p.__call__()