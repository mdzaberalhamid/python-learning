# Python - List Comprehension
print("Python - List Comprehension:")

# Without using list comprehension
print("\nWithout using list comprehension:")
list_1 = ['apple', 'mango', 'banana', 'malta', 'cherry']
list_2 = []

for x in list_1:
  if 'm' in x:
    list_2.append(x)

print(list_2)

# Using list comprehension
print("\nUsing list comprehension:")

list_3 = ['apple', 'mango', 'banana', 'malta', 'cherry']
list_4 = [i for i in list_3 if 'm' in i]
print(list_4)

# Another example of using list comprehension
print("\nAnother example of using list comprehension:")

list_5 = [
  'apple', 'apple', 'banana', 'malta', 'apple', 'orange', 'cherry', 'mango',
  'apple'
]
list_6 = [j for j in list_5 if j == 'apple']
list_7 = [k for k in list_5 if k != 'apple']
print(list_6)
print(list_7)

# With no if statement
print("\nWith no if statement:")
list_8 = [l for l in list_5]
print(list_8)

# Iterable
print("\nIterable:")

print("Example 1:")
list_9 = [m for m in range(10)]
print(list_9)

print("Example 2:")
list_10 = [n for n in range(10) if n < 5]
print(list_10)

# Expression
print("\nExpression:")

# Example 1
print("Example 1:")

list_11 = ['toyota','mazda','nissan']
list_12 = [o.upper() for o in list_11]
print(list_12)

# Example 2
print("Example 2:")
list_13 = ['hi' for p in list_11]
print(list_13)

# Example 3
print("Example 3:")
list_14 = ['apple','banana','mango','cherry','banana']
list_15 = [q if q != 'banana' else 'orange' for q in list_14]
print(list_15)
