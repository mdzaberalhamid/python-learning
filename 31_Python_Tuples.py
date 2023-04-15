# Python Tuples
print("Python Tuples:")

# Tuple
print("\nTuple:")
tuple1 = ('apple', 'banana', 'mango')
print(tuple1)

# Tuple item
print("\nTuple Item:")
tuple2 = ('red', 'green', 'blue')
print(tuple2[1])

# Allow duplicate values
print("\nAllow duplicate values:")
tuple3 = (3, 7, 1, 9, 9, 4, 3, 3, 5, 3)
print(tuple3)

# Tuple length
print("\nTuple length:")
print(len(tuple3))

# Tuple with one item
print("\nTuple with one item:")

tuple4 = ("Toyota", )
print(type(tuple4))  # class tuple
# if comma not included
ex1 = ("Toyota")
print(type(ex1))  # class string

# Tuple items data types
print("\nTuple items data types:")

print("Example 1:")
tuple5 = (1, 2, 3, 4, 5)
tuple6 = ("one", "two", "three")
tuple7 = (True, True, False)
print(tuple5)
print(tuple6)
print(tuple7)

print("Example 2:")
tuple8 = ("chess", 1, True, 5, "world")
print(tuple8)

# The tuple() constructor
print("\nThe tuple() constructor:")
tuple8 = tuple(('test', 'result', 'evaluation'))
print(tuple8)
print("")
