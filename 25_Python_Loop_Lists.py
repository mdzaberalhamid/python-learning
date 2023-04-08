# Python - Loop Lists
print("Python - Loop Lists:")

# Loop through a list
print("\nLoop through a list:")
list_1 = [1, 2, 3, 4, 5]
for x in list_1:
  print(x)

# Loop through using index no
print("\nLoop through using index no:")
list_2 = ['maclaren', 'toyota', 'nissan']
# print(len(list_2))
for i in range(len(list_2)):
  # print(i)
  print(list_2[i])

# Looping with while loop
print("\nLooping with while loop:")
list_3 = ['chess', 'cricket', 'tennis', 'golf']
a = 0
while a < len(list_3):
  print(list_3[a])
  a = a + 1

# Looping using list comprehension
print("\nLooping using list comprehension:")
list_4 = ['red', 'green', 'blue']
[print(j) for j in list_4]
