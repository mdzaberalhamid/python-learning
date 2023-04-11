# Python - Sort Lists
print("Python - Sort Lists:")

# Sort List Alphanumerically
print("\nSort List Alphanumerically:")

print("Example 1:")
list_1 = ['red', 'blue', 'yellow', 'green']
list_1.sort()
print(list_1)

print("Example 2:")
list_2 = [65, 90, 1, 5, 9, 36, 87]
list_2.sort()
print(list_2)

# Sort in descending order
print("\nSort in descending order:")

print("Example 1:")
list_3 = ['toyota', 'nissan', 'volvo', 'ford']
list_3.sort(reverse=True)
print(list_3)

print("Example 2:")
list_4 = [2, 7, 8, 17, 25, 13, 10, 99]
list_4.sort(reverse=True)
print(list_4)

# Customizing sort function
print("\nCustomizing sort function:")

def demoF1(n):
  return abs(n - 50)

list_5 = [100, 50, 65, 82, 23]
list_5.sort(key=demoF1)
print(list_5)

# Case insensitivity sorting
print("\nCase insensitivity sorting:")

print("Example 1:")
list_6 = ["banana", "Orange", "KIWI", "cherry"]
list_6.sort()
print(list_6)

print("Example 2:")
list_6.sort(key=str.lower)
print(list_6)

# Reverse Order
print("\nReverse Order:")
list_7 = ['mango', 'banana', 'pineapple', 'date']
list_7.reverse()
print(list_7)
