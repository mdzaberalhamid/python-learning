# Python Lists
print("Python Lists:")

# A list
print("\nA List:")
mylist = ['apple', 'banana', 'watermelon']
print(mylist)

# Allows duplicate values
print("\nAllows duplicate values:")
mylist_2 = ['toyota', 'BMW', 'lamborghini', 'toyota', 'BMW']
print(mylist_2)

# List length
print("\nList length:")
print(len(mylist_2))  # 5

# List items data types
print("\nList items data types:")
list_1 = ['chess', 'football', 'golf']
list_2 = [1, 5, 9]
list_3 = [True, False, False]
print(list_1)
print(list_2)
print(list_3)

# Different data types in one list
print("\nDifferent data types in one list:")
list_4 = ['lenovo', 2014, True]
print(list_4)

# Type
print("\nType:")
list_5 = ['volvo', 'nissan', 'mazda']
print(list_5)
print(type(list_5))

# The list() constructor
print("\nThe list() constructor:")

newList = list(('item1', 'item2', 'item3'))
print(newList)
