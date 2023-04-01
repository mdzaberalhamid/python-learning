# Python Strings

# Strings
print('Hello World!')
print("String 1")
print("")

# Assigning string to a variable
txt2 = "String 2"
print(txt2)
print("")

# Multi-line string
txt3 = """String 3: Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(txt3)
print("")

# Strings are arrays
txt4 = "Learning Python Programming!"
print(txt4[0])
print(txt4[9])
print("")

# Lopping through string
for x in "chess":
  print(x)

print("")

# Check string for a word
txt5 = "This products price is free!"
print("free" in txt5)
print("giveaway" not in txt5)

# or
if "free" in txt5:
  print("Word found!")

if "giveaway" not in txt5:
  print("Word not found.")

print("")

# String length
txt6 = "Lorem ipsum dolor sit amet"
print(len(txt6))
print("")
