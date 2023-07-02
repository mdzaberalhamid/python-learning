# Python String Formatting
print("Python String Formatting\n")

print("String format()")

print("\nExample:")
price = 50
txt = "The item is {} dollars."
print(txt.format(price))

print("\nExample:")
price2 = 20
txt2 = "The price is {:0.2f} dollars."
print(txt2.format(price2))

print("\n")
print("Multiple values:")

print("\nExample:")
quantity = 3
itemno = 1
cost = 15
myorder = "I want {} pieces of itemno {} for {:0.2f} dollars."

print(myorder.format(quantity,itemno,cost))

print("\n")
print("Index Numbers:")

print("\nExample:")
name = "Zaber"
age = 30
txt3 = "His name is {0} and age is {1} years."
print(txt3.format(name,age))

print("\nExample:")
txt4 = "His name is {0}. \n{0} is {1} years old."
print(txt4.format(name, age))

print("")
print("Named Indexes")

print("\nExample")
myorder2 = "I have a {carname} car. It is a {model}."
print(myorder2.format(carname="Ford", model="Mustang"))
