# Python Iterators
print("Python Iterators:\n")

# Returning an iterator from a tuple
mytuple = ('apple', 'banana', 'mango')
myit = iter(mytuple)

# And printing each value
print(next(myit))
print(next(myit))
print(next(myit))

print("\n")

# Strings are also iterable objects
mystr = "ZABER"
it2 = iter(mystr)
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

print("\n")


# Creating an Iterator
class MyNumbers:

  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x


myclass = MyNumbers()
iter1 = iter(myclass)

print(next(iter1))
print(next(iter1))
print(next(iter1))

print("\n")


# StopIteration
class MyNumbersFixed:

  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 8:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration


myclass = MyNumbersFixed()
iter1 = iter(myclass)
for m in iter1:
  print(m)
