# Make counting easy
t = (1,2,3,4)
for x in t:
    print(x)

# Lists, Tuples, dictionaries and Sets are all iterable objects
people = ['Darvesh', 'Rahul', 'Vikas']
i = iter(people)
print(i)
print(next(i))
print(next(i))
print(next(i))
#print(next(i))          # Stop Iteration

# Iterable Class
import random
class Lottery:
    def __init__(self):
        self._max = 5

    def __iter__(self):
        # The yield statement suspends function's execution and sends a value back to the caller
        # but retains enough state to enable function to resume where it is left off

        for _ in range(self._max):
            yield random.randrange(0,100)

    def setMax(self, value):
        self._max = value

print('-'*20)
Lottery = Lottery()
Lottery.setMax(50)

for x in Lottery:
    print(x)

print('-'*20)



