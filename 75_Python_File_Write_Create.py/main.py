# Python File Write
print("Python File Write\n")

# Write(append) to an existing file, then open and read the file after appending
print(
  "Write(append) to an existing file, then open and read the file after appending:"
)
print("Example:")
f1 = open("demofile1.txt", "a")
f1.write("\nThis is some added text.")
f1.close()

f1 = open("demofile1.txt", "r")
print(f1.read())

# Overwrite a file content, then open and read the file after overwriting
print(
  "\nOverwrite a file content, then open and read the file after overwriting:")
print("Example:")
# f2 = open("demofile2.txt", "r")
# print(f2.read())
f2 = open("demofile2.txt", "w")
f2.write("New text after overwritting!")
f2.close()

f2 = open("demofile2.txt", "r")
print(f2.read())

# Creating a New File
print("\nCreating a New File:")
print("Example:")
f3 = open("newfile.txt","x")  # create a file
f3.write("Some new contents inside the new file!")
f3.close()

f3 = open("newfile.txt","r")
print(f3.read())