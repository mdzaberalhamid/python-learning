# Python - Copy Dictionaries
print("Python - Copy Dictionaries:")

# Copying a dictionary
print("\nCopying a dictionary:")

# Using copy() method
car1 = {"brand": "Mazda", "model": "A", "serial": 1111}
car2 = car1.copy()
print(car2)

# Using dict() function
car3 = dict(car1)
print(car3)
