# Python Read Files
print("Python Read Files\n")

# Reading a File
print("Reading a File:\n")

print("Example:")
f = open("demofile.txt", "r")
print(f.read())

print("")
print("Example:")
f2 = open("folder1/demofile2.txt", "r")
print(f2.read())

# Reading parts of a File
print("\nReading parts of a File:\n")

print("Example:")
f3 = open("demofile.txt", "r")
print(f3.read(6))  # Hello!

print("")
# Reading a line
print("Reading a line:\n")

print("Example:")
f4 = open("demofile.txt")
print(f4.readline())

print("")
# Looping through the file line by line
print("Looping through the file line by line:\n")
print("Example:")
f5 = open("demofile.txt", "r")
for x in f5:
  print(x)

print("")
# Close Files
print("Close Files:\n")
f5.close()