class Student:
  __name="Hello"                          # Private Variable
  def __init__(self):                     # Contructore
    print(self.__name)                    # Using private variable within constructor
    self.__displayinfo()                  # Using encapsulated method within constructor
  def __displayinfo(self):                # Create an encapsulated method
    print("Welcome to the Python World")

obj=Student()                             # Calling the Constructor. So it will give output for name & displayinfo both.
