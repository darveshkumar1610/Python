# A string is a sequence of characters which can be created by enclosing characaters inside single/double quotes
# Triple quotes can be used to represent multiline strings.
# Immutable
# Space will be included in length or range

### use ctrl+? to comment out all the lines in a file.

### String Indexing
# Left-to-Right (start with 0)
# Right-to-Left (start with -1)

w="Welcome to the world"
print(w[6])
print(w[-1])

### Slicing
print(w[0:7])     # Welcome
print(w[0:])      # It will read complete line
print(w[0::2])    # with 2 increment

print(w[-1::-2])  # Reverse decrement

### String Iteration
w="Welcome to the world"
t=len(w)
print(t)
for a in range(t)
  print(w[a])

for a in range(t-1,-1,-1):
  print(w[a])
  
# direct method without range.
  for a in w:
  print(a)
  
### String functions - lower(), upper(), title(), capitalize(), find(), index(), isalpha(), isdigit(), isalnum()
w="Welcome to the World"
n=w.lower()
print(n)

u=w.upper()
print(u)

t=w.title()
print(t)

c=w.capitalize
print(c)

w="Welcome"
print(w.find('e',2))    # 2 is the start position of index counting
print(w.find('z',2))

# find will give result as -1 if character not found in a string but index() will give runtime error.
print(w.index('e',2))
print(w.find('z'))

## isalpha = if string contains only alphabets = TRUE
## isdigit = if string contains only digits/numbers = TRUE
## is alnum = if string contains either alphabet or digit = TRUE (False if anything else e.g. space or @)
w="Welcome123"
print(w.isaplha())
print(w.isdigit())
print(w.isalnum())

## String function: chr() - Convert an integer to ASCII caharacter and ord() - Reverse of chr(). 
## Input will be only single character.
y = chr(65)
print(y, type(y))

y = ord('A')
print(y, type(y))

## String function: format()
## The format method formats the specified value(s) and insert them inside the string's placeholder.
## The placeholder is defined using curly braces {}.

# named indexes
txt1="Welcome to {fname}{lname}".format(fname="the",lname="world")
# numbered indexes
txt2="Welcome to {0}{1}".format("the","world")
# empty placeholders
txt3="Welcome to {}{}".format("the","world")
print(txt1)
print(txt2)
print(txt3)

txt1="Welcome to {a:10}{b}".format(a="XX",lname="YY")         # To limit the placeholder length as 10 character out of which 2 are already used by a placeholder.
txt1="Welcome to {a:^10}{b}".format(a="XX",lname="YY")        # To put the value of a in the CENTRE of placeholder's length.
txt1="Welcome to {a:>10}{b}".format(a="XX",lname="YY")        # To put the value of a in the RIGHT of placeholder's length.
txt1="Welcome to {a:<10}{b}".format(a="XX",lname="YY")        # To put the value of a in the LEFT of placeholder's length.
