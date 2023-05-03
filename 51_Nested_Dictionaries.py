# Python - Nested Dictionaries
print("Python - Nested Dictionaries")

# Nested dictionary
print("\nNested dictionary:")
print("\nExample 1:")
cars = {
  "car1": {
    "brand": "toyota",
    "year": 1980
  },
  "car2": {
    "brand": "volvo",
    "year": 1990
  },
  "car3": {
    "brand": "man",
    "year": 2000
  }
}
print(cars)

print("\nExample 2:")

s_car1 = {"brand": "ferrari", "year": 2010}
s_car2 = {"brand": "marcedes", "year": 2020}
s_car3 = {"brand": "lamborghini", "year": 2023}

sportscars = {"sportscar1": s_car1, "sportscar2": s_car2, "sportscar3": s_car3}

print(sportscars)

# Accessing items of a nested dictionary
print("\nAccessing items of a nested dictionary:")

print(cars["car3"]["brand"])
print(cars["car3"]["year"])

print(sportscars["sportscar2"]["brand"])
print(sportscars["sportscar2"]["year"])
