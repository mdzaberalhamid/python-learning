# Python - Loop Dictionaries
print("Python - Loop Dictionaries:")

# Looping through a dictionary
print("\nLooping through a dictionary:")
print("\nExample 1:")
car = {"brand": "ford", "model": "F", "year": 2000}

for x in car:
  print(x)

print("\nExample 2:")
for x in car:
  print(car[x])

print("\nExample 3:")
# Using the values() method
for x in car.values():
  print(x)

print("\nExample 4:")
# Using the keys() method
for x in car.keys():
  print(x)

# Looping through both keys and values
print("\nLooping through both keys and values:")
for x, y in car.items():
  print(x, y)
