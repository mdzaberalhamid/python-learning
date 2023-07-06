# Python Delete File
print("Python Delete File:\n")
# Importing os
import os

# Deleting a file
# os.remove("demofile.txt")

# Checking if file exist
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("File doesn't exist!")

# Deleting a folder
os.rmdir("demofolder")