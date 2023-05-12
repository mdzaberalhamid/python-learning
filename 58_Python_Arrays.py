# Python Arrays
print("Python Arrays")

print("Example")
cars = ['Toyota', 'Mazda', 'Nissan']
print(cars)

print("\nAccessing elements of an array")
print("Example")
c = cars[0]
print(c)

print("\nModify a value")
print("Example")
cars[0] = 'Volvo'
print(cars[0])
print(cars)

print("\nLength of an array")
print("Example")
l = len(cars)
print(l)

print("\nLooping array elements")
print("Example")
for x in cars:
  print(x)

print("\nAdd an element")
print("Example")
cars.append('ford')
print(cars)

print("\nRemoving array elements")
print("Example")
cars.pop(1)
print(cars)
print("Example")
cars.remove('ford')
print(cars)
