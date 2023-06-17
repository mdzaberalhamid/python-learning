# Python Modules
print("Python Modules:\n")

# Importing my created module
import mymodule

mymodule.greeting("Arfi")

personName = mymodule.dict1["name"]
personAge = mymodule.dict1["age"]
print(personName)
print(personAge)

# Re-naming a Module
import mymodule2 as m2

x1 = m2.list1
print(x1)

# Built-in Modules
import platform

x2 = platform.system()
print(x2)

# Using the dir() Function
# x3 = dir(platform)
# print(x3)

# Test my module with dir()
x4 = dir(mymodule)
print(x4)

# Import From Module
# Importing parts from a module
from mymodule import tuple1

print(tuple1)

# Another example
from mymodule import dict1

x5 = dict1["country"]
print(x5)
