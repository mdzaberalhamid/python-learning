# Python While Loops
print("Python While Loops")

# The while loop
print("\nThe while loop")
i = 1
while i < 10:
  print(i)
  i += 1

# The break statement
print("\nThe break statement")
m = 1
while m < 5:
  print(m)
  if m == 3:
    break
  m += 1

# The continue statement
print("\nThe continue statement")
n = 0
while n < 5:
  n += 1
  if n == 4:
    continue
  print(n)

# The else statement
print("\nThe else statement")
x = 1
while x < 6:
  print(x)
  x += 1
else:
  print("x is no longer less than 6")
