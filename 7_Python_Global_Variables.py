# Python - Global Variables

# Creating global and local variable
txt = 'learn'  # global variable

def function1():
  txt = 'use'  # local variable
  print('Python is easy to ' + txt)  # Python is easy to use

function1()

print('Python is easy to ' + txt)    # Python is easy to learn
print("")

# Using global keyword
# Changing a local variable to a global variable
def function2():
  global a
  a = 'Python'
  # print(a)

function2()
print(a + " is awesome")             # Python is awesome
print("")

# Changing the value of a global variable inside a function
x = 1

def function3():
  global x
  x = 5

function3()

print("Value of x is:", x)           # Value of x is: 5
