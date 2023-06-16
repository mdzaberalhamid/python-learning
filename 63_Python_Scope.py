# Python Scope
print("Python Scope:\n")

# Local Scope
print("Local Scope")
print("Example 1")

def myfunction():
  x = 100  # local variable
  print(x)

myfunction()
# print(x)  # error

print("\nFunction inside function scope:")
print("Example 2")

def myfunction2():
  y = 25

  def myinnerfunction():
    print(y)

  myinnerfunction()

myfunction2()

print("\nGlobal Scope")
print("Example 3")
z = 1  # global variable

def myfunction3():
  print(z)

myfunction3()

print(z)

# Naming Variables
print("\nNaming Variables")
print("Example 4")
m = 25

def myfunction4():
  m = 5
  print(m)

myfunction4()
print(m)

# Global Keyword
print("\nGlobal Keyword")
print("Example 5")

def myfunction5():
  global n
  n = 10
  print(n)

myfunction5()
print(n)

# Changing a global var value inside a scope
print("\nExample 6")
o = 400

def myfunction6():
  global o
  o = 500
  print(o)

myfunction6()
