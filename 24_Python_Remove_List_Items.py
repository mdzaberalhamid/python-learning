# Python - Remove List Items

# Remove an item from list
print("Remove an item from list:")
list_1 = ['apple', 'mango', 'banana']
print(list_1)
list_1.remove('banana')
print(list_1)

# Remove a list item using index no
print("\nRemove a list item using index no:")
print("Example 1:")
list_2 = ['toyota', 'marcedes', 'ford']
print(list_2)
list_2.pop(1)
print(list_2)

print("Example 2:")
list_3 = ['red', 'green', 'blue', 'yellow']
print(list_3)
list_3.pop()
print(list_3)

# Using del keyword
print("\nUsing del keyword:")

print("Example 1:")
# Remove a list item using del keyword
list_4 = list_3
print(list_4)
del list_4[0]
print(list_4)

print("Example 2:")
# Delete a list using del keyword
list_5 = ['a', 'b', 'c']
print(list_5)
del list_5
# print(list_5)  # error

# Clear a list
print("\nClear a list:")
list_6 = [1, 2, 3, 4, 5, 6]
print(list_6)
list_6.clear()
print(list_6)
