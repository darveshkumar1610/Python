### A function is a block of statements which can be used repititively in a program to save developer's time.
### We can pass data known as parameters(arguments) into a function. Funtion is defined by 'def' keyword.

# Simple function

def simplefunction():           # define the function
  print("Welcome to the Python world")

simplefunction()                # Calling the function
simplefunction()

Welcome to the Python world     # Output
Welcome to the Python world
#################################################
# Function with arguments

def sumfunction(a,b):       # define the function
  print(a+b)

sumfunction(20,30)            # Call the function
sumfunction(40,10)
#################################################
# Function with deafult arguments/parameter

def sumfunction(a,b=5):       # define the function
  print(a+b)

sumfunction(20)            # Call the function

#################################################
# Function with RETURN

def sumfunction(a,b=5):       # define the function
  c = a+b
  return c                    # store the result and do not print on console

output = sumfunction(20, 10)            # Call the function
print(output)

###############
def square(x):
  return x*x

s = square(5)
print(s)
