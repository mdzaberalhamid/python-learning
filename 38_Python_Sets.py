# Python - Sets
print("Python - Sets:")

# Creating a set
print("\nCreating a set:")

set1 = {'a', 'b', 'c'}
print(set1)

# Duplicate values in a set will be ignored
print("\nDuplicate values in a set will be ignored:")

set2 = {True, True, False}
print(set2)

# True and 1 is considered same value in set
print("\nTrue and 1 is considered the same value:")

set3 = {'apple', True, 1, 5}
print(set3)

# Get length of a set
print("\nGet length of a set:")

set4 = {1, 4, 7, 3, 6, 9, 15, 22, 30, 99}
print(len(set4))

# Set items - Data types
print("\nSet items - Data types:")

# int
print("int")
set5 = {1, 2, 3, 4, 5}
print(set5)

# string
print("string")
set6 = {'apple', 'mango', 'orange'}
print(set6)

# boolean
print("boolean")
set7 = {True, True, False}
print(set7)

# mix data types
print("mix data types")
set8 = {2, 'apple', True, 9, False, 'orange'}
print(set8)

# Get the type
print("\nGet the type:")
set9 = {'toyota', 'nissan', 'volvo'}
print(type(set9))

# The set() constructor
print("\nThe set() constructor:")

set10 = set((3, 'test', False))
print(set10)
print(type(set10))
