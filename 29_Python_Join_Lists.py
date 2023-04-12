# Python - Join Lists
print("Python - Join Lists:")

# Joining two lists
print("\nJoining two lists:")
print("Example 1:")
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

print("Example 2:")
list4 = ['red', 'green', 'blue']
list5 = [False, True, True]
for x in list5:
  list4.append(x)

print(list4)

print("Example 3:")
list6 = [7, 8, 9]
list7 = ['toyota', 'nissan', 'audi']
list6.extend(list7)
print(list6)
