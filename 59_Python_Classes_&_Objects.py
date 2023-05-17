# Python Classes and Objects
print("Python Classes and Objects:")

# Creating a class
print("\nCreating a class:")

class c1:
  x = 25

print(c1)

# Creating an object
print("\nCreating an object:")

object1 = c1()
print(object1.x)

# The __init__() Function
print("\nThe __init__() Function:")

class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

person1 = Person("Zaber", 29)

print(person1.name)
print(person1.age)

# The __str__() Function
print("\nThe __str__() Function:")

class Car:

  def __init__(self, brand, year):
    self.brand = brand
    self.year = year

  def __str__(self):
    return f"{self.brand}({self.year})"

car1 = Car("Toyota", 1990)

print(car1)

# Object methods
print("\nObject methods:")

class SoftwareEngineer:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myFunction(self):
    print("Hi, I am " + self.name)

engineer1 = SoftwareEngineer("Zaber", 29)
engineer1.myFunction()

engineer2 = SoftwareEngineer("Zaheed", 39)
engineer2.myFunction()

# Modifying an object property
print("\nModifying an object property:")
print(engineer2.age)

engineer2.age = 45
print(engineer2.age)

# Delete an object property
del engineer1.age
# print(engineer1.age)  # error

# Delete object
del engineer2
# print(engineer2.name)  # error

# The pass statement
print("\nThe pass statement:")

class Demo:
  pass

print("Nothing in the class Demo!")
