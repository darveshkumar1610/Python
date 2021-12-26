#########################################################################################
############### Overloading (Same function with multiple parameters) ####################
#########################################################################################

class A:
  def displayinfo(self,name=""):          # Same function with multiple parameters
    print("Welcome to the python"+name)


obj=A()
obj.displayinfo()                         # Parameter may not be provided.
obj.displayinfo("World")                  # Parameter may be provided.

######################################

class Area:
  def calculate_area(self,a=None,b=None):
    
    if a!=None and b!=None:
      print("Area of the Rectangle: ", (a*b))
    elif a!=None:
      print("Area of the Square: ", (a*a))
    else:
      print("Nothing to calculate")

obj1=Area()
obj1.calculate_area()
obj1.calculate_area(10)
obj1.calculate_area(10,20)

#########################################################################################
###################################### Overriding #######################################
#########################################################################################

class A:                                  # Parent Class
  def displayinfo(self):
    print("Welcome to the Python World")
    
class B(A):                               # Child Class
  def displayinfo(self):
    super().displayinfo()                 # Calling Parent Class function in Child Class function.
    print("Welcome to Learning Python")
    
obj=B()
obj.displayinfo()

############################################

class A:
  def showData(self):
    print("This is from A Class")

class B(A):
  def showData(self):
    print("This is from B Class")
    
obj=B()
obj.showData()
