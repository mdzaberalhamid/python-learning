# Python Booleans
print("Python Booleans")

# example 1
print("Example 1")
print(10 > 8)  # true
print(5 < 9)  # true
print(2 == 3)  # false
print("")

# example 2
print("Example 2")
num1 = 99
num2 = 33

if num1 > num2:
  print("Number 1 is bigger.")
else:
  print("Number 1 is smaller.")

print("")

# evaluate values
print("Evaluate values:")
print(bool("This is a string"))  # true
print(bool(10))  # true
print("")

# evaluate variables
print("Evaluate variables:")
a1 = 5
a2 = 1
print(bool(a1))  # true
print(bool(a2))  # true
print("")

# most values are true except some
print("Most values are true except some:")
txt1 = "Hi"
print(bool(txt1))  # true
txt2 = ""
print(bool(txt2))  # false
x1 = 25
print(bool(x1))  # true
x2 = 0
print(bool(x2))  # false
l1 = ['apple', 'mango', 'watermelon']
print(bool(l1))  # true
l2 = []
print(bool(l2))  # false
print("")

# the false values
print("The false values:")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool({}))
print(bool([]))

print("")

# functions can return a boolean
print("Functions can return a boolean:")

# example 1
print("Example 1:")

def function1():
  return True

result = function1()
print(result)  # true

# example 2
print("Example 2:")

def function2():
  return False

if function2():
  print("Yes!")
else:
  print("No.")  # No

print("")

# using a built-in function
print("Using a built-in function:")

z = 1000
print(isinstance(z, int))  # true
print("")
