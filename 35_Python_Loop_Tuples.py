# Python - Loop Tuples
print("Python - Loop Tuples:")

# Looping through a tuple
print("\nLooping through a tuple:")

tuple1 = (1, 2, 3, 4, 5)
for num in tuple1:
  print(num)

# Looping using index number
print("\nLooping using index number:")
tuple2 = ('apple', 'banana', 'cherry', 'date', 'mango', 'pineapple')

for i in range(len(tuple2)):
  print(tuple2[i])

# Looping with while loop
print("\nLooping with while loop:")
tuple3 = ('red', 'green', 'blue', 'white', 'yellow')

x = 0
while x < len(tuple3):
  print(tuple3[x])
  x += 1
