# Python - Change List Items
print("Python - Change List Items:")

# Change List Item Value
print("\nChange List Item Value:")

list1 = ['mango', 'cherry', 'banana']
list1[1] = 'date'
print(list1)

# Change a Range of List Item Values
print("\nChange a Range of List Item Values:")

list2 = ['toyota', 'mazda', 'nissan', 'audi', 'BMW']

# Example 1
print("\nExample 1:")
list2[2:4] = ['volvo', 'marcedes']
print(list2)

# Example 2
print("\nExample 2:")
list2[1:3] = ['ferrari', 'ford', 'bugatti']
print(list2)

# Example 3
print("\nExample 3:")
list2[1:4] = ['porche']
print(list2)

# Insert Items to a List
print("\nInsert Items to a List:")

list3 = ['red', 'yellow', 'blue']
list3.insert(1, 'green')
print(list3)
