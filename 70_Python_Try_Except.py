# Python Try Except
print("Python Try Except")

# Exception Handling
print("\nException Handling:")
print("Example:")
try:
  print(x)
except:
  print("An exception occurred.")

# Many Exceptions
print("\nMany Exceptions:")
print("Example:")
try:
  print(x)
  # print("x" + 10)
except NameError:
  print("x is not defined!")
except:
  print("Something else is wrong.")

# Using Else
print("\nUsing Else:")
print("Example:")
try:
  print("Hi")
except:
  print("Something went wrong!")
else:
  print("Nothing went wrong!")

# Finally block
print("\nFinally block:")
try:
  print(x)
except:
  print("Something went wrong!")
finally:
  print("The 'try except' is finished.")

# Raising an exception
print("\nRaising an exception:")
print("Example 1:")
x = -1
if x < 0:
  # pass
  raise Exception("Oops, number is below 0.")

print("Example 2:")
num = "hi"

if not type(num) is int:
  pass
  # raise TypeError("Only integers allowed!")
