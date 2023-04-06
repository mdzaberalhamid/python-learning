# Python - Access List Items
print("Python - Access List Items:")

# Access list items
print("\nAccess list items:")

list1 = ['apple', 'banana', 'cherry']
print(list1)

print(list1[0])  # apple
print(list1[2])  # cherry

# Access items by negative indexing values
print("\nAccess items by negative indexing values:")

list2 = ['volvo', 'nissan', 'toyota', 'audi', 'BMW']
print(list2)

print(list2[-3])  # toyota
print(list2[-2])  # audi

# Range of Indexes
print("\nRange of Indexes:")

list3 = ['mango', 'banana', 'strawberry', 'apple', 'orange', 'lemon', 'cherry']
print(list3)

print(list3[2:5])
print(list3[:3])
print(list3[3:])

print(list3[-6:-1])
print('apple' in list3)  # True

if 'banana' in list3:
  print("Banana is listed!")
