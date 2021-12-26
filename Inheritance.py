############################################################
################# Single-Level Inheritance #################
############################################################

class A:
  def displayA(self):             # Self is the argument here which is mandatory
    print("Welcome to the Python World - A")

class B(A):
  def displayB(self):
    print("Welcome to the Python World - B")
    
obj=B()                           # Create Object for B Class and call for any Class object
obj.displayA()
obj.displayB()

############################################################
################# Multi-Level Inheritance ##################
############################################################

class A:
  def displayA(self):             # Self is the argument here which is mandatory
    print("Welcome to the Python World - A")

class B(A):
  def displayB(self):
    print("Welcome to the Python World - B")

class C(B):
  def displayC(self):
    print("Welcome to the Python World - C")    

obj=C()                           # Create Object for C Class and call for any Class object
obj.displayA()
obj.displayB()
obj.displayC()

############################################################
################## Multiple Inheritance ####################
############################################################
class A:
  def displayA(self):             # Self is the argument here which is mandatory
    print("Welcome to the Python World - A")

class B(A):
  def displayB(self):
    print("Welcome to the Python World - B")

class C(A,B):
  def displayC(self):
    print("Welcome to the Python World - C")    

obj=C()                           # Create Object for C Class and call for any Class object
obj.displayA()
obj.displayB()
obj.displayC()
