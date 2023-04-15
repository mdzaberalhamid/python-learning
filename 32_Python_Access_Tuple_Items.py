# Python - Access Tuple Items
print("Python - Access Tuple Items:")

# Access tuple items
print("\nAccess tuple items:")
tuple1 = (1, 2, 3)
print(tuple1)
print(tuple1[1])  # 2

# Negative indexing
print("\nNegative indexing:")
tuple2 = ('toyota', 'volvo', 'nissan')
print(tuple2)
print(tuple2[-1])  # nissan

# Range of indexes
print("\nRange of indexes:")
tuple3 = ('apple', 'cherry', 'mango', 'banana', 'date', 'orange')
print(tuple3)

print("Example 1:")
print(tuple3[2:5])

print("Example 2:")
print(tuple3[:2])

print("Example 3:")
print(tuple3[1:])

# Range of negative indexes
print("\nRange of negative indexes:")
tuple4 = ('green', 'blue', 'red', 'yellow', 'orange')
print(tuple4[-3:-1])

# Check a tuple item existence
print("\nCheck a tuple item existence:")
tuple5 = ('C', 'C++', 'Java')
print(tuple5)
if 'Java' in tuple5:
  print("Yes, Java is in the list!")
