# Python - List Methods
print("Python - List Methods:")
print("")

# append()
print("append() method:")
list1 = ['apple', 'banana', 'mango']
list1.append("orange")
print(list1)
print("")

# clear()
print("clear() method:")
list2 = [2, 4, 7, 8, 10, 26]
print(list2)
list2.clear()
print(list2)
print("")

# copy()
print("copy() method:")
x = ['chess', 'golf', 'tennis']
list3 = x.copy()
print(list3)
print("")

# count()
print("count() method:")
list4 = ['apple', 'mango', 'apple', 'apple', 'banana']
print(list4.count('apple'))
print("")

# extend()
print("extend() method:")
list5 = ['red', 'green', 'blue']
a = ['yellow']
list5.extend(a)
print(list5)
print("")

# index()
print("index() method:")
list6 = ['toyota', 'BMW', 'ford']
print(list6.index('BMW'))
print("")

# insert()
print("insert() method:")
list7 = ['True', 'False', 'False']
list7.insert(1, True)
print(list7)
print("")

# pop()
print("pop() method:")
list8 = [3, 5, 7, 8, 10]
list8.pop(4)
print(list8)
print("")

# remove()
print("remove() method:")
list9 = ['red', 'violet', 'orange']
list9.remove('violet')
print(list9)
print("")

# reverse()
print("reverse() method:")
list10 = ['volvo', 'mazda', 'ferrari']
list10.reverse()
print(list10)
print("")

# sort()
print("sort() method:")
list11 = [2, 5, 8, 10, 33, 12, 28, 99, 1, 15]
list11.sort()
print(list11)
list11.sort(reverse=True)
print(list11)
print("")
