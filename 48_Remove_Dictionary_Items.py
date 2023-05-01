# Python - Remove Dictionary Items
print("Python - Remove Dictionary Items:")

# Removing items
print("\nRemoving items:")
player = {"name": "John", "age": 25, "height": 5.6}

# Example 1
print("\nExample 1:")
print(player)
player.pop("age")
print(player)

# Example 2
print("\nExample 2:")
chair = {"brand": "A", "size": "small", "price": 100, "installment": False}
print(chair)

chair.popitem()
print(chair)

# Example 3
print("\nExample 3:")
print(chair)
# Using del keyword
del chair["size"]
print(chair)

# Deleting a dictionary
print("\nDeleting a dictionary:")
print(chair)
del chair
# print(chair)  # error

# Empty a dictionary
print("\nEmpty a dictionary:")
print(player)
player.clear()
print(player)
