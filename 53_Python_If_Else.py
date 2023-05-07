# Python If ... Else
print("Python If ... Else")

# If
print("\nIf...")
# Example 1
print("Example 1:")
a = 25
b = 99
if a < b:
  print("a is less than b")

# Elif
print("\nElif...")
# Example 2
print("Example 2:")
c = 33
d = 33
if c > d:
  print("c is greater than d")
elif c == d:
  print("c and d is equal!")

# Else
print("\nElse...")
# Example 3
print("Example 3:")
e = 100
f = 100
if e > f:
  print("e is greater than f")
elif e < f:
  print("e is less than f")
else:
  print("e is equal to f")

# Short hand if
print("\nShort hand if...")
# Example 4
print("Example 4:")
a1 = 5
b1 = 2

if a1 > b1: print("a1 is bigger")

# Short hand if...else
print("\nShort hand if...else")
print("Example 5:")
a2 = 99
b2 = 9

print("A2") if a2 > b2 else print("B2")

print("Example 6:")
a3 = 3
b3 = 3
print(">") if a3 > b3 else print("<") if a3 < b3 else print("=")

# And
print("\nAnd...")
print("Example 7:")
x = 25
y = 5
z = 1993

if x > y and z > y:
  print("Both condition is True.")

# Or
print("\nOr...")
print("Example 8:")

if y > x or z > x:
  print("Only one condition is True.")

# Not
print("\nNot...")
print("Example 9:")

if not x > z:
  print("x is not greater than z")

# Nested if
print("\nNested if...")
print("Example 10:")
m = 33
if m > 10:
  print("Value is:", m)
  print("Value is greater than 10")
  if m < 20:
    print("But, value is less than 20")
  else:
    print("Also, value is greater than 20")

# The pass statement
print("\nThe pass statement:")
print("Example:")

p, q = 2, 1
if p > q:
  pass
# Error will not occur
