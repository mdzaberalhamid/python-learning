# Python - Add Set Items
print("Python - Add Set Items:")

# Add items to a set
print("\nAdd items to a set:")
set1 = {'A', 'B', 'C', 'D'}
set1.add('E')
print(set1)

# Add sets
print("\nAdd sets:")
set2 = {'toyota','mazda','ford'}
addset = {'nissan','volvo'}
set2.update(addset)
print(set2)

# Add any iterable(list,tuple,dict)
print("\nAdd any iterable:")
set3 = {"apple","banana","cherry"}
list1 = ["mango","date"]

set3.update(list1)
print(set3)
