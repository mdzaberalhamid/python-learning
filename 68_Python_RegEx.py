# Python RegEx
print("Python RegEx")

print("\nRegEx in Python")
# regex module
import re

# Example 1
print("Example 1")
# Checking if a string starts with "The" and ends with "Spain"
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("Yes, we have a match.")
else:
  print("No match.")

# regex functions
print("\nRegEx Functions\n")
print("findall()")

y = re.findall("ai", txt)
print(y)

print("")
print("search()")
z = re.search("\s", txt)
# print(type(z))

print(z.start())

print("")
print("split()")
# Spliting the string at every white-space character
m = re.split("\s", txt)
print(m)

print("")
print("sub()")
# Replacing every white-space character with underscore
n = re.sub("\s", "_", txt)
print(n)

# Match Object
print("\nMatch Object")

print("\nExample 1")
txt2 = "This is Some text."
o = re.search("text", txt2)
print(o)

print("\nExample 2")
d = re.search(r"\bS\w", txt2)
print(d.span())

print("\nExample 3")
e = re.search(r"\bS\w", txt2)
print(e.string)
