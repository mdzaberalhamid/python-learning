# Python - Set Methods
print("Python - Set Methods:")

print("")
print("add() method:")
set1 = {'apple', 'mango', 'banana'}
set1.add('orange')
print(set1)

print("")
print("clear() method:")
set2 = {1, 4, 6, 9}
set2.clear()
print(set2)

print("")
print("copy() method:")
set3 = {'toyota', 'volvo', 'nissan'}
x = set3.copy()
print(x)

print("")
print("difference() method:")
set4 = {'red', 'green', 'blue'}
set5 = {'blue', 'violet', 'yellow'}
y = set4.difference(set5)
print(y)

print("")
print("discard() method:")
set6 = {5, 2, 3, 7, 9, 0}
set6.discard(0)
print(set6)

print("")
print("intersection() method:")
set7 = {'apple', 'banana', 'mango'}
set8 = {'mango', 'date', 'orange'}
z = set7.intersection(set8)
print(z)

print("")
print("issubset() method:")
set9 = {'a', 'b', 'c'}
set10 = {'m', 'n', 'o', 'c', 'd', 'a', 'b'}
e = set9.issubset(set10)
print(e)

print("")
print("issuperset() method:")
set11 = {1, 2, 3, 4, 5, 6}
set12 = {4, 5, 6}
f = set11.issuperset(set12)
print(f)

print("")
print("pop() method:")
set13 = {'red', 'green', 'blue'}
set13.pop()
print(set13)

print("")
print("remove() method:")
set14 = {'toyota', 'nissan', 'volvo'}
set14.remove('volvo')
print(set14)

print("")
print("symmetric_difference() method:")
set15 = {3, 4, 5}
set16 = {3, 6, 7, 8, 9}
g = set15.symmetric_difference(set16)
print(g)

print("")
print("union() method:")
set17 = {'a', 'b', 'c'}
set18 = {'d', 'e'}
h = set17.union(set18)
print(h)

print("")
print("update() method:")
set19 = {'apple', 'banana', 'date'}
set20 = {'apple', 'orange', 'mango'}
set19.update(set20)
print(set19)
