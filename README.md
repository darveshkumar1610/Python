# Python
# Install Pycharm for Python
- Create the First Python ''Hello World'' Program using Print Function

# Variables in Python
  - Never start with Number or special character except underscore(_)
  - Never have space in between
    - Memory address assigned to Values
    - To get the memory address use print(id(a))

# Operators in Python
 - Arithmetic Operators in Python (+, -, *, /, % Modulus, ** Exponents, // Floor division)
 - Assignment Operators in Python
 - Comparison Operators in Python
 - Logical Operators in Python
 - Membership Operators in Python
 - Identity Operators in Python
 - Bitwise Operators in Python

# Data Types in Python
  - Numeric
    - Int
    - Float
    - Complex Numbers
  - Sequence
    - String
    - List (Mutable)
    - Tuple
  - Dictionary (Mutable)
  - Set (Unique items)

# User Input & Type Casting (conversion) in Python
  - input() - To take an input from user at the runtime which will be a STRING always.
      a = input("Enter the value: ")
      print(a)
      
  - int() - Convert an input into float
      a = int(input("Enter the value1: "))
      b = int(input("Enter the value2: "))
      print(a+b)
      
  - float() - Convert an input into float
  - eval() - Convert an input into int/float/binary
 
 # Conditional Statements in Python (Indentation must have same space/tab)
 - If (For single condition)
    if [conditional expression]:
      [statement(s) to be exceuted]
      
    a = int(input("Enter the value: "))
    if a%2==0:
      print(a, "is an Even Number")
      
 - If Else (For two conditions)
    if [conditional expression]:
      [statement(s) to be exceuted]
    else:
      [alternate statement(s) to be exceuted]
      
    a = int(input("Enter the value: "))
    if a%2==0:
      print(a, "is an Even Number")
    else:
      print(a, "is an Odd Number")
      
 - If-Elif-else (For Mulitple Conditions)
    if [condition#1]:
      [execution statement#1]
    elif [condition#2]:
      [execution statement#2]
    elif [condition#3]:
      [execution statement#3]
    else:
      [exection statement when if and elif(s) are FALSE]
      
    marks = 55
    if marks >= 60:
      print("First Division")
    elif marks >= 50:
      print("Second Division") 
    elif marks >= 35:
      print("Third Division") 
    else:
      print("Fail")
      
 - How to Build a Simple Calculator in Python (simpleCalculator.py)


# Loops
 - For Loop with Range() in Python
    - range for increment (start position, condition (less-than no.), increment by)
        - range with one parameter: range(5) = range(0, <5, 1) => 0,1,2,3,4 (Start with 0, run till (5-1) with increment of 1)
        - range with two parameter: range(1, 6) = range(1, <6, 1) => 1,2,3,4,5 (Start with 1, run till (6-1) with increment of 1)
        - range with three parameter: range(1,6,2) = range(1, <6, 2) => 1,3,5 (Start with 1, run till (6-1) with increment of 2)
     - range for decrement (start position always > than condition number, condition (run till n-1), increment by must be always -1)
        
 - While Loop in Python

# Strings in detail
 - String Concatenation in Python (string + string)
 - String Indexing & String Slicing in Python
 - String Iteration in Python
 - Lower, Upper, Title & Capitalize String Functions in Python
 - Find, Index, Isalpha, Isdigit & Isalnum String Functions in Python
 - Ord() and Chr() Functions in Python
 - String Format () Method in Python

# List in Detail
 - List in Python
 - List Iteration in Python
 - List Function - (Pop, Remove & Clear) List Method
 - Python List Comprehension - Elegant way to Create Lists
 - (Pop, Remove & Clear) List Method
 - Count, Max, Min, Sort, Reverse & Index List Function
 - Zip Function - Iterate Over 2+ Lists at the Same Time
 - Python Program to Convert String to a List
 - Implement a Stack and Queue Using a List Data Type

# Dictionary in Detail
 - Introduction to Dictionary in Python
 - Dictionary Function & Method in Python
 - Python Nested Dictionary

# Tuple in Detail
 - Tuple in Python (Single value will not be a tuple)
 - Iteration (With len() and range() function OR with using tuple directly)
 - Tuple Functions: 
   - min() - Print the min number from the tuple elements. 
   - max() - Print the max number from the tuple elements. 
   - count() - how much time an element exists in tuple, 
   - index() - Print the index number of an element in the tuple 
   - sum() - Sum of all the elements (int or float only) in tuple

# Set in Detail
 - Sets in Python
   - Unordered, unindexed, unique data, no duplicates (will be removed automatically)
   - written in curly braces e.g. {10,20,30,40}
   - Iteration will be using for loop directly on set and not using indexes.
 - Set Functions in Python
   - set() - To convert a list or tuple into set.
   - add() - Add a new element into existing set.
   - pop() - Delete an element from a set without indexing/value. It can show the element to be deleted.
   - remove() - Remove a specified valued element from set, if element does not exist, it will raise an error.
   - discard() - Remove a specified valued element from set, if element does not exist, it will NOT raise any error. 
   - clear() - Clear all the elements from a set and print set().
   - update() - Add new elements in a set with unique values.

# User Defined Functions in Python
  - simple function
  - function with arguments
  - return type

# Modules in Python
 - Math Module in Python (https://docs.python.org/3.7/library/math.html)
   - math.ceil(): return the ceiling of x, the smallest integer >= x. If x is not float, delegates to x.__ceil__() which returns an integral value.
   - math.floor(): return the floor of x, the largest integer <= x. If x is not float, delegates to x.__floor__() which returns an integral value.
   - math.fabs(): return the absolute value of x.
   - math.factorial(): return x factoriak as an integer. Raises Value Error if x is not integral or is negative.
   - math.fsum(list/tuple): retrun an accurate floating point sum of all the elements in the iterable (list/tuple).
   - math.sqrt(): return the sqaure root of an integer.
 - Random Module in Python (Generate random numbers)
   - random.randint(a,b): return a number between a and b (both included).
   - random.randrange(a,b): return a numbers between a (included) and b (not included).
   - random.choice(l): return a random element from a list.
   - random.random(): returns a random float number between 0 & 1.
   - random.shuffle(l): Takes a sequence and returns the sequence in a random order.
   - random.uniform(a,b): returns a random float number between two given numbers.
 - Datetime Module in Python
   - datetime.datetime.now(): return current date and time containing year, month, day, hr, min, sec and microsecond.
   - datetime.datetime.now.strftime(%Y): Separate year, month, day, hr, min, sec from current time.
   - datetime.datetime(2021,12,25): create date objects date with time.
 - Python - Random Number Guessing Game (Using Random Modeul)
 - Python - Rock, Paper, Scissors Game (Using Random Module)
 - Pickle Module
   - dump()
   - load()

# JSON in Python
  - Convert JSON Data to Python Object
      - json.dumps(): convert dictionary to json.
      - json.loads(): convert json to dictionary.
  - Reading and Writing JSON File in Python

# Object Oriented Programming (Class (Variables/Attributes and Methods/function) & Object/Instance of a Class)
 - Object Oriented Programming (Methods & Constructors)
   - Methods need to call with objects but Constructors (__init__) do not need to call.
 - Inheritance in Python
   - Single: where B (Child) class will inherit the properties of A (Parent)
   - Multi-Level: where B(Parent) class will inherit the properties of A(Grandparent) & C(Child) will inherit the properties of B(Parent).
   - Multiple: where C(Child) class can inherit the properties of A(Grandparent) & B(Parent).
 - Encapsulation in Python: 
   - An Objects variables should not always be directly accessible. 
   - The methods can ensure the correct values are set. If an incorrect value is set, the method can return an error.
 - Getter and Setter Method in Python
 - Polymorphism in Python: Same function name (but different signatures) being used for different types. E.g. len() function for list & string.
   - Overloading Method: function with multiple parameters.
   - Overriding Method: Same function in 2 Inherittted classes. The Parent Class function can be called in Child class function using super() function.
     It mostly used for memory reducing processing as it need to call one child function only.
 - Bike Rental System

# Python Errors and Built-in Exceptions
  - Python Exception Handling (with TRY and ACCEPT)
    - Syntax Errors: can not handled automatically. We have to resolve Syntax errors.
    - Logical Errors (Exceptions): Can be handled.
      - ZeroDivisionError: a=10 print(a/10)
      - NameError: print(b)
      - TypeError: print('10'+10)
      - ValueError: a=int(input("Enter the value"))
      - IndexError: l=[1,2,3,4] print(l[4])
      - KeyError: d={'name':'Testing','fee':5000} print(d[fees])
      - ModuleNotFound: When using module which is not build or available
      - ImportError: When using a function which is not available in module.

# Python - SQLite (DB Create and Connection)
 - Python: Installing DB Browser for SQLite
   - Search for DB Browser for sqlite in google and download for 64-bit Windows
   - Install DB Browser > Install anyway > Next > Accept > Next > Next > Finish
   - Open sqlite.db file in DB Browser
 - Insert Query - SQLite
 - Select Query, Order By & Limit
 - SQLite Delete Query
 - SQLite Update Query
 - SQLite WHERE Clause
 - SQLite JOIN (sqlite3.OperationalError: RIGHT and FULL OUTER JOINs are not currently supported.)
   - (INNER) JOIN: Returns records that have only matching values in both the tables
   - LEFT(OUTER)JOIN: Returns all records from the LEFT table and the matched records from the RIGHT table.
   - RIGHT(OUTER)JOIN: Returns all records from the RIGHT table and the matched records from the LEFT table.
   - FULL(OUTER)JOIN: Returns all records when there is a match in either LEFT or RIGHT table

# Download and Install XAMPP on Windows - PyMySQL
 - install pymysql package "pip install pymysql"
   - Start Apache and MySQL in XAMPP Control Panel and Open localhost/phpmyadmin in the web browser
 - Python: Creating MySQL Database & Connection (mysql.py)
 - MySQL Data Types
   - TINYINT (till 3 digit)
   - INT (till 11 digit)
   - BIGINT (till 20 digit)
   - VARCHAR (0-255)
   - TEXT (0-60000)
   - LONGTEXT ()
   - DATE (YYYY-MM-DD)
   - DATETIME (YYYY-MM-DD HH:MM:SS)
   - TIMESTAMP (Current Time)
   - TIME (HH:MM:SS)
   - YEAR (YYYY)

# Python MySQL Operations
 - MySQL Create Table Query using Python
 - MySQL Insert Query using Python
 - MySQL Select Query using Python
 - MySQL Delete Query using Python
 - MySQL Update Query using Python
 - Python MySQL Order By & Limit
 - Python MySQL Searching & Filter Data
 - Python MySQL Joins Complete Introduction
 - MySQL INNER JOIN
 - MySQL LEFT JOIN
 - MySQL RIGHT JOIN
 - MySQL EQUI JOIN
 - MySQL Self Join & Full Outer Join
 - MySQL BETWEEN Operator
 - Use of MIN and MAX Functions
 - MySQL GROUP BY Statement
 - MySQL: Distinct Keyword
 - MySQL SUM () Function
 - MySQL AVG() Function
 - MySQL COUNT() Function
 - MySQL - IN or Not IN Operators
