# Python Datetime
print("Python Datetime:")

# Python dates
print("\nPython dates:")

import datetime

t = datetime.datetime.now()
print(t)

# Date output
print("\nDate output:")

print(t.year)
print(t.strftime("%A"))  # Day name

# Creating a date object
print("\nCreating a date object:")

newdate = datetime.datetime(1993, 5, 25)
print(newdate)

# The strftime() method
print("\nThe strftime() method:")

print(t.strftime("%d"))  # Date
print(t.strftime("%B"))  # Month
print(t.strftime("%Y"))  # Year
