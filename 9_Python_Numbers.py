# Python Numbers

x = 1
y = 3.98
z = 5j

print(x)  # 1
print(type(x))  # int
print(y)  # 3.98
print(type(y))  # float
print(z)  # 5j
print(type(z))  # complex
print("")  # blank line

# int
num1 = 763524760902
num2 = -9712547
num3 = 1542
print(num1)  # 763524760902
print(num2)  # -9712547
print(num3)  # 1542
print("")

# float
f1 = 5.1
f2 = -8.73546
print(f1)  # 5.1
print(f2)  # -8.73546

f3 = 5e3
f4 = 12E4
print(f3)  # 5000.0
print(f4)  # 120000.0
print("")

# complex
c1 = 2 + 9j
print(c1)  # (2 + 9j)
print("")

# type conversion
t1 = 1
t2 = float(t1)
print(t1)  # 1
print(t2)  # 1.0
print("")

t3 = 3.76
t4 = int(t3)
print(t3)  # 3.76
print(t4)  # 3
print("")

t5 = 6
t6 = complex(t5)
print(t5)  # 6
print(t6)  # (6 + 0j)
print("")

# Random number
import random

print(random.randrange(1, 100))  # a random number between 1 to 100
