#To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

#Create a class named Student, which will inherit the properties and methods from the Person class:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

#Now the Student class has the same properties and methods as the Person class.

#Use the Student class to create an object, and then execute the printname method:

x = Student("Mike", "Olsen")
x.printname()