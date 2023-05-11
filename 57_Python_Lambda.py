# Python Lambda
print("Python Lambda")

print("\nExample 1")
x = lambda d: d * 3
print(x(1))
print(x(2))
print(x(3))

print("\nExample 2")
y = lambda e, f: e + f
print(y(3, 1))
print(y(3, 5))
print(y(2, 5))

print("\nExample 3")
z = lambda g1, g2, g3: g1 + g2 + g3
print(z(1, 2, 3))
print(z(4, 5, 6))
print(z(7, 8, 9))

print("\nUsing inside a function:")
print("\nExample 4")


def function1(n):
  return lambda h: h * n


dodouble = function1(2)

print(dodouble(11))
print(dodouble(27))
print(dodouble(50))
print(dodouble(512))

print("\nExample 5")


def f2(n):
  return lambda i: i * n


tripler = f2(3)

print(tripler(3))
print(tripler(9))
print(tripler(15))

print("\nExample 6")


def myfunction(n):
  return lambda j: j * n


mydoubler = myfunction(2)
mytripler = myfunction(3)

print(mydoubler(2))
print(mydoubler(5))

print(mytripler(5))
print(mytripler(10))
