# Python - Remove Set Items
print("Python - Remove Set Items:")

# Removing items
print("\nRemoving items:")

print("Example 1:")
set1 = {'apple', 'cherry', 'orange'}
print(set1)

set1.remove('cherry')
print(set1)

print("Example 2:")
set2 = {'volvo', 'toyota', 'nissan', 'ford'}
print(set2)

set2.discard('ford')
print(set2)

# Removing a random item
print("\nRemoving a random item:")
set3 = {'red', 'green', 'blue'}
x = set3.pop()
print(x)
print(set3)

# Empty and delete a set
print("\nEmpty and delete a set:")

set4 = {1, 3, 4, 6, 8, 9, 0}
set4.clear()
print(set4)

set5 = {'x', 'y', 'z'}
print(set5)
del set5
# print(set5)  # error
