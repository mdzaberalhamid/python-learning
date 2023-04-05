# Python Operators
print("Python Operators:")

# Example
print("\nExample:")
print(5 + 10)  # 15

# Arithmetic Operators
print("\nArithmetic Operators:")

print(6 + 3)  # 9
print(9 - 5)  # 4
print(4 * 2)  # 8
print(8 / 4)  # 2
print(7 % 3)  # 1
print(2**3)  # 8
print(9 // 2)  # 4

# Assignment Operators
print("\nAssignment Operators:")

x1 = 1
print(x1)  # 1
x1 += 2
print(x1)  # 3
x1 -= 1
print(x1)  # 2
x1 *= 4
print(x1)  # 8
x1 /= 2
print(x1)  # 4

x1 %= 3
print(x1)  # 1
x1 = x1 + 1
x1 **= 5
print(x1)  # 32

# Comparison Operators
print("\nComparison Operators:")

a = 9
b = 5
print(a == b)  # False
print(a != b)  # True
print(a > b)  # True
print(a < b)  # False
print(a >= b)  # True
print(a <= b)  # False

# Logical Operators
print("\nLogical Operators:")

c = 10
print(c > 5 and c < 20)  # True
print(c > 5 or c > 15)  # True
print(not (c > 5 or c > 15))  # False

# Identity Operators
print("\nIdentity Operators:")
d1 = ["apple", "mango"]
d2 = ["apple", "mango"]
d3 = d1

print(d1 is d3)  # True
print(d1 is d2)  # False

# Comparing with == operator
print(d1 == d2)  # True

# Membership Operators
print("\nMembership Operators:")

e = ['ferrari', 'nissan', 'toyota']
print('toyota' in e)  # True
print('audi' not in e)  # True
print('audi' in e)  # False

# Bitwise Operators
# Bitwise operators compare binary numbers
print("\nBitwise Operators:")

print(6 & 3)  # 2
print(6 | 3)  # 7
print(6 ^ 3)  # 5
# 6 = 0000000000000110
# 3 = 0000000000000011
# --------------------
# 2 = 0000000000000010

print(~3)  # -4
# Inverted 3 becomes -4:
#  3 = 0000000000000011
# -4 = 1111111111111100

# ---------------------
#  0 = 0000000000000000
# -1 = 1111111111111111
# -2 = 1111111111111110
# -3 = 1111111111111101
# -4 = 1111111111111100

print(3 << 2)  # 12
# Inserting two 0's to the right and removing two 0's from the left of the binary value of 3, then calculate the new value
# 0000000000000011 = 3
# 0000000000001100 = 12

print(8 >> 2)  # 2
# # Inserting two 0's to the left and removing two 0's from the right of the binary value of 8, then calculate the new value which is 2
# 0000000000001000 = 8
# 0000000000000010 = 2

# Operator Precedence
print("\nOperator Precedence:")

# Example 1
print("Example 1:")

print((6 + 3) / 3 * (2 + 1))  # 9/3*3 = 9
print((6 + 3) / (3 * (2 + 1)))  # 9/(3*3) = 1

# Example 2
print("Example 2:")
print(80 + 5 * 4)  # 80 + 20 = 100

# Precedence order
print("\nPrecedence order:")
print("()")
print("**")
print("+x -x ~x")
print("* / // %")
print("+ -")
print("<< >>")
print("&")
print("^")
print("|")
print("== != > >= < <= is is not in not in")
print("not")
print("and")
print("or")

# Same precedence example
print("\nSame precedence example:")
print(6 + 3 - 7 + 8)  # 10
