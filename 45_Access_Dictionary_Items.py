# Python - Access Dictionary Items
print("Python - Access Dictionary Items:")

# Accessing items
print("\nAccessing items:")
print("Example 1:")
d1 = {"name": "Zaber", "age": 29, "id": 1}
print(d1["name"])
print(d1["age"])

print("Example 2:")
print(d1.get("id"))

# Get keys
print("\nGet keys:")
print("Example 1:")
print(d1.keys())

print("Example 2:")
car = {"brand": "toyota", "model": "x", "year": 1980}
print(car.keys())

car["color"] = "white"
print(car.keys())

# Get values
print("\nGet values:")
print("Example 1:")

laptop = {"brand": "Lenovo", "color": "black", "year": 2014}
print(laptop.values())

print("Example 2:")
laptop["OS"] = "Windows"
print(laptop.values())
laptop["year"] = 2013
print(laptop.values())

# Get items
print("\nGet items:")
print("Example 1:")
player = {"name": "John", "height": 5.6, "hair": "black"}
print(player.items())

print("Example 2:")
player["weight"] = 60
print(player.items())

# Checking if a key is available
print("\nChecking if a key is available:")
game1 = {"event": "chess", "time": 14.00}
print(game1)
if "time" in game1:
  print("Yes, \"time\" key is found.")
