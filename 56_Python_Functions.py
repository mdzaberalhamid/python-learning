# Python Functions
print("Python Functions")

# Creating a function
print("\nCreating a function")


def function1():
  print("Hi, from a Function!")


# Calling the function
function1()

# Arguments
print("\nArguments")


def function2(name):
  print("Hi,", name)


function2("Zaber")
function2("Asif")
function2("Sajal")

# Number of arguments
print("\nNumber of arguments")


def function3(fname, lname):
  # print("Hi,", fname, lname)
  print("Hi," + " " + fname + " " + lname + "!")


function3('Md', 'Zaber')
function3('Md', 'Muttakin')

# Arbitrary arguments, *args
print("\nArbitrary arguments, *args")


def function4(*players):
  print(players)
  print("Top player:", players[0])


function4('Zaber', 'Sajal', 'Asif', 'Muttakin')

# Keyword arguments
print("\nKeyword arguments")

def function5(fruit2,fruit1):
  print(fruit1, "should be in every list.")

function5(fruit2 = 'Banana', fruit1 = 'Apple')

# Arbitrary keyword arguments, **kwargs
print("\nArbitrary keyword arguments, **kwargs")

def function6(**car):
  print(car)

function6(brand='Toyota',color='Blue',year='1993')
function6(brand='Nissan',color='Silver',year='1999')

# Default parameter value
print("\nDefault parameter value")

def function7(country='Bangladesh'):
  print("I am from " + country)

function7()
function7("Canada")
function7("Italy")

# Passing a list as an argument
print("\nPassing a list as an argument")

colors = ['red','green','blue']

def function8(color):
  # print(color)
  for x in color:
    print(x)

function8(colors)

# Return values
print("\nReturn values")

def function9(num):
  return num * 3

print(function9(3))
print(function9(5))
print(function9(9))
print(function9(9)+function9(1))

# The pass statement
print("\nThe pass statement")
def function10():
  pass

function10()  # Error will not occur

# Recursion
print("\nRecursion")

def try_recursion(k):
  print(k)
  if k > 0:
    try_recursion(k-1)

try_recursion(3)
