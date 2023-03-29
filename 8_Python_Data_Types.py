# Python Data Types

# Getting the data type
x = 1
print(type(x))
print("")

# Data types
a = 10
b = "Hello World!"
c = 3.45
d = 1j
e = ['Mango', 'Banana', 'Watermelon']
f = ('Ferrari', 'BMW', 'Nissan')
g = range(5)
h = {"name": "Zaber", "age": 29}
i = {"Apple", "Cherry", "Grape"}
j = frozenset({"Android", "Windows", "iOS"})
k = True
l = b'World'
m = bytearray(5)
n = memoryview(bytes(5))
o = None

print(type(a))  # int
print(type(b))  # str
print(type(c))  # float
print(type(d))  # complex
print(type(e))  # list
print(type(f))  # tuple
print(type(g))  # range
print(type(h))  # dict
print(type(i))  # set
print(type(j))  # frozenset
print(type(k))  # bool
print(type(l))  # bytes
print(type(m))  # bytearray
print(type(n))  # memoryview
print(type(o))  # NoneType
print("")

# Setting specific data type
p = int(5)
print(p)
print(type(p))  # int

q = list(('Audi','Marcedes','Toyota'))
print(q)
print(type(q))  # list

r = dict(name='Zaber',age=29)
print(r)
print(type(r))  # dict

s = set(("Red","Green","Blue"))
print(s)
print(type(s))  # set
