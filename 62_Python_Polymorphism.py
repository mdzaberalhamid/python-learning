# Python Polymorphism
print("Python Polymorphism:\n")

# Function Polymorphism
print("Function Polymorphism:\n")
# len()

x = "Hello World"
print(len(x))  # Number of characters

mytuple = ('apple', 'banana', 'mango', 'date')
print(len(mytuple))  # Number of items

mydict = {"brand": "Toyota", "model": 1980, "color": "white"}
print(len(mydict))  # Number of key/value pairs

# Class Polymorphism
print("\nClass Polymorphism:\n")

# Same move() method in all classes
class Car:

  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:

  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:

  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
  x.move()

# Inheritance Class Polymorphism
print("\nInheritance Class Polymorphism:\n")

class Vehicle:

  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):

  def move(self):
    print("Sail")

class Plane(Vehicle):

  def move(self):
    print("Fly!")

car2 = Car("Toyota", "Z")
boat2 = Boat("Ibiza", "Touring 22")
plane2 = Plane("Cessena", "X")

for x in (car2, boat2, plane2):
  print(x.brand)
  print(x.model)
  x.move()
