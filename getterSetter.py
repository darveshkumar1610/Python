class Student:
  def __init__(self):           # Constructor
    self.__name=""              # Create private variable (name)
  def getname(self):            # Get the variable
    return self.__name
  def setname(self,name):       # Set the variable to use
    self.__name=name
    
  obj=Student()                 # Call Object
  obj.setname("Testing")        # Set the value to setname
  name=obj.getname()
  print(name)
