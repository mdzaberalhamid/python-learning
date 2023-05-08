# Python For Loops
print("Python For Loops")

# for loop
print("\nfor loop")
print("Example:")
fruits = ['apple', 'banana', 'mango']
for x in fruits:
  print(x)

# Looping through a string
print("\nLooping through a string")
print("Example:")
for x in "car":
  print(x)

# The break statement
print("\nThe break statement")
print("Example:")
car = ['toyota', 'mazda', 'nissan']
for x in car:
  print(x)
  if x == 'mazda':
    break

# The continue statement
print("\nThe continue statement")
print("Example:")
values = [1, 2, 3, 4, 5]
for x in values:
  if x == 2:
    continue
  print(x)

# The range() function
print("\nThe range() function")

print("Example:")
for x in range(4):
  print(x)

print("Example:")
for x in range(2, 5):
  print(x)

print("Example:")
for x in range(3, 12, 3):
  print(x)

# Else in for loop
print("\nElse in for loop")
print("Example:")
for x in range(4):
  print(x)
else:
  print("Loop finished!")

# Nested loop
print("\nNested loop")
print("Example:")
colors = ['red', 'green']
fruits = ['apple', 'cherry']
for a in colors:
  for b in fruits:
    print(a, b)

# The pass statement
print("\nThe pass statement")
print("Example:")
for x in [0, 1, 2]:
  pass
# Error will not occur
