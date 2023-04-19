# Python - Unpack Tuples
print("Python - Unpack Tuples:")

# Unpacking a tuple
print("\nUnpacking a tuple:")

tuple1 = ('apple', 'banana', 'mango')
a, b, c = tuple1
print(a)
print(b)
print(c)
# print(a, b, c)

# Using an asterisk
print("\nUsing an asterisk:")

# Example 1
print("\nExample 1:")
tuple2 = ('toyota', 'nissan', 'mazda', 'ford')
x, y, *z = tuple2
print(x)
print(y)
print(z)

# Example 2
print("\nExample 2:")
tuple3 = ('red', 'green', 'blue', 'yellow', 'white')
p, *q, r = tuple3
print(p)
print(q)
print(r)
