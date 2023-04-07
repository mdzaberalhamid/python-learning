# Python - Add List Items
print("Python - Add List Items:")

# Appending items to a list
print("\nAppending items to a list:")

list_1 = ['toyota', 'nissan', 'mazda']
list_1.append('ford')
print(list_1)

# Inserting items to a list
print("\nInserting items to a list:")
list_1.insert(2, 'porche')
print(list_1)

# Extending a list
print("\nExtending a list:")
list_2 = ['red', 'green', 'blue']
list_extra = ['yellow', 'violet', 'orange']
list_2.extend(list_extra)
print(list_2)

# Adding other iterable object(tuple,set,dict)
print("\nAdding other iterable object:")
list_3 = ['chess', 'golf', 'tennis']
tuple_1 = ('badminton', 'football', 'cricket')

list_3.extend(tuple_1)
print(list_3)
