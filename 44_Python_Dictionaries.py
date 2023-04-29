# Python Dictionaries
print("Python Dictionaries:")

# Creating a dictionary
print("\nCreating a dictionary:")

d1 = {"brand": "toyota", "color": "black", "year": 1980}
print(d1)

# Dictionary items
print("\nDictionary items:")
print(d1["brand"])

# Dictionary length
print("\nDictionary length:")
print(len(d1))

# Dictionary items data types
print("\nDictionary items data types:")
d2 = {
  "brand": "marcedes",
  "electric": False,
  "year": 1993,
  "color": ["red", "green", "blue"]
}

print(d2)

# type()
print("type()")
print(type(d2))

# The dict() constructor
print("\nThe dict() constructor:")

d3 = dict(name="Zaber", age=29, country="Bangladesh")
print(d3)
