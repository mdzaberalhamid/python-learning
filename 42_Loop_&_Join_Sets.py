# Python - Loop Sets
print("Python - Loop Sets:")

# Loop items
print("\nLoop items:")

set1 = {'apple', 'banana', 'mango'}
for x in set1:
  print(x)

# Python - Join Sets
print("\nPython - Join Sets:")

# Join two sets
print("\nJoin two sets:")
print("Example 1:")
set2 = {1, 4, 5, 7, 8}
set3 = {2, 3, 6, 9}

set4 = set2.union(set3)
# print(set2)
print(set4)

print("Example 2:")
set5 = {'toyota', 'nissan'}
set6 = {'volvo', 'mazda'}

set5.update(set6)
print(set5)

# Keeping only the same value
print("\nKeeping only the same value:")
set7 = {'google', 'facebook', 'apple'}
set8 = {'apple', 'banana', 'date'}

set7.intersection_update(set8)
print(set7)
# set7.intersection(set8)
# print(set7)

# Keeping all except the duplicates
print("\nKeeping all except the duplicates:")
set9 = {'apple', 'mango', 'orange'}
set10 = {'apple', 'google', 'amazon'}

set9.symmetric_difference_update(set10)
print(set9)

set11 = set9.symmetric_difference(set10)
print(set11)

# True and 1 is same
print("\nTrue and 1 is same:")
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)
print(z)
