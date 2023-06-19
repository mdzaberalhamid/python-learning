# Python JSON
print("Python JSON\n")

# JSON in Python
print("JSON in Python:")
import json

# Parse JSON - Convert from JSON to Python
print("\nParse JSON - Convert from JSON to Python")
print("Example:")
# some json
j = '{"name":"Zaber","age":30,"city":"Sylhet"}'
# parsing j
x = json.loads(j)
# result is a python dictionary
print(x)
print(type(x))
print(x["name"])
print(x["age"])

# Converting from Python to JSON
print("\nConvert from Python to JSON")
print("Example:")

# a python object (dict)
d = {"name": "Zaber", "age": 30, "maritalstatus": "unmarried"}
# converting into json
y = json.dumps(d)

# result is a json string
print(y)
print(type(y))

# More examples
print("\nMore examples")

print(json.dumps({"name": "Jahi", "age": 18}))
print(json.dumps(['apple', 'banana', 'mango']))
print(json.dumps(('chess', 'cricket', 'tennis')))
print(json.dumps("This is a string"))
print(json.dumps(25))
print(json.dumps(3.14159))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Another example
print("\nAnother example")
c = {
  "name": "Zaber",
  "age": 30,
  "married": False,
  "pets": None,
  "cars": [{
    "brand": "tesla",
    "sl no.": 1
  }, {
    "brand": "marcedes",
    "sl no.": 2
  }]
}
# print(c)
# converting to json
pytojson = json.dumps(c)
print(pytojson)
print(type(pytojson))

# Formatting the result
print("\nFormatting the result")
print("Example:")
pytojson2 = json.dumps(c, indent=4)
print(pytojson2)

# Ordering the result
print("\nOrdering the result")
pytojson3 = json.dumps(c, indent=2, sort_keys=True)
print(pytojson3)
