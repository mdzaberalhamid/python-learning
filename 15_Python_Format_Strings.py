# Python - Format Strings

# string format
# example 1
age = 29
txt = "Hi, I am Zaber and my age is {}"
print(txt.format(age))

# example 2
quantity = 3
itemno = 789
price = 50

myorder1 = "I want {} pieces of item {} for {} dollars."
print(myorder1.format(quantity, itemno, price))

# example 3
price = 80
itemno = 190
quantity = 5

myorder2 = "I need item no {2} of {1} pieces for {0} dollars."
print(myorder2.format(price, quantity, itemno))
