### First we should have module1.py file which contains different function (sum, multiply)
### Another user.py file will use the module and its functions

# module1.py
def sum(a,b):
  c=a+b
  return c

def mul(a,b):
  c=a*b
  return c

# user.py
import module1
print(module1.sum(10,20))

## Now run user.py script on command line.
###########################################################
# user.py
import module1 as m
print(m.sum(10,20))
print(m.mul(10,20))

## Now run user.py script on command line.
###########################################################
from module1 import sum
print(sum(10,20))

## Now run user.py script on command line.
###########################################################
from module1 import *
print(sum(10,20))
print(mul(10,20))

## Now run user.py script on command line.
