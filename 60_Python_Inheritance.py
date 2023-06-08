# Python Inheritance
print("Python Inheritance:\n")

# Creating a parent class


class Person:

  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


# Creating an object using the Person class

object1 = Person('MD', 'Zaber')

# Executing the printname method
object1.printname()

print("\n")


# Creating a child class
class Student(Person):
  pass


# Creating an object from the child class
student1 = Student('John', 'Doe')
student2 = Student('Mike', 'Olsen')

# Executing printname method
student1.printname()
student2.printname()

print("\n")


# Adding the __init__() Function
class Army(Person):

  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)


army1 = Army('Jack', 'Dalton')
army2 = Army('Dale', 'Barbie')

army1.printname()
army2.printname()

print("\n")


# Using the super() Function
class Engineer(Person):

  def __init__(self, fname, lname):
    super().__init__(fname, lname)


engineer1 = Engineer('Saad', 'Araf')
engineer1.printname()

print("\n")


# Adding Properties i.e serial
class Instructor(Person):

  def __init__(self, fname, lname, serial):
    super().__init__(fname, lname)
    self.serial = serial


instructor1 = Instructor('Abdur', 'Rahman', 5)
instructor1.printname()
print(instructor1.serial)

print("\n")


# Adding Methods
class Driver(Person):

  def __init__(self, fname, lname):
    super().__init__(fname, lname)

  def welcome(self):
    print('Welcome to', self.firstname, self.lastname, 'in our company!')


d1 = Driver('Chanchal', 'Biswas')
d1.printname()
d1.welcome()
print("\n")
