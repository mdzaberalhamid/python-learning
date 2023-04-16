# Python - Update Tuples
print("Python - Update Tuples:")

# Changing tuple values
print("\nChanging tuple values:")
tuple1 = ('apple', 'banana', 'date')
list1 = list(tuple1)
# print(list1)
list1[1] = 'mango'
tuple1 = tuple(list1)
print(tuple1)

# Adding items
print("\nAdding items:")
tuple2 = ('toyota', 'mazda', 'nissan')
list2 = list(tuple2)
list2.append('ford')
# print(list2)
tuple2 = tuple(list2)
print(tuple2)

# Adding tuple to a tuple
print("\nAdding tuple to a tuple:")
tuple3 = (2, 5, 8, 13, 20)
tuple_extra = (23, )
tuple3 += tuple_extra
print(tuple3)

# Remove items
print("\nRemove items:")
tuple4 = ('red', 'green', 'blue', 'cyan')
list4 = list(tuple4)
# print(list4)
list4.remove('cyan')
tuple4 = tuple(list4)
print(tuple4)

# Deleting a tuple
print("\nDeleting a tuple:")
tuple5 = (True, False, False)
del tuple5
# print(tuple5)  # Error
