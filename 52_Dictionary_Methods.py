# Python Dictionary Methods
print("Python Dictionary Methods:")

# Dictionary Methods
print("\nDictionary Methods:\n")

# clear() method
print("clear() method:")
car = {"brand": "toyota", "model": "X", "year": 1990}
print(car)
car.clear()
print(car)

# copy() method
print("")
print("copy() method:")
d1 = {"brand": "Lenovo", "serial": 123}
d2 = d1.copy()
print(d2)

# fromkeys() method
print("")
print("fromkeys() method:")
a = ('key1', 'key2', 'key3')
b = 0
d3 = dict.fromkeys(a, b)
print(d3)

# get() method
print("")
print("get() method:")
truck = {"brand": "MAN", "model": "X", "year": 2000}
print(truck)
print(truck.get("brand"))

# items() method
print("")
print("items() method:")
print(truck.items())

# keys() method
print("")
print("keys() method:")
print(truck.keys())

# pop() method
print("")
print("pop() method:")
truck.pop("model")
print(truck)

# update() method
print("")
print("update() method:")
truck.update({"color": "green"})
print(truck)

# values() method
print("")
print("values() method:")
print(truck.values())
