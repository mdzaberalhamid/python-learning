# Python - String Methods

# capitalize()
str1 = "python is easy to learn."
print(str1.capitalize())
print("----------")

# center()
str2 = "center"
print(str2.center(20))
print("")

# count()
str3 = "I like chess, because I am a chess player. And, I believe chess is fun to play."
print(str3.count("chess"))  # 3
print("")

# endswith()
str4 = "Data is correct"
print(str4.endswith("correct"))  # True
print(str4.endswith("wrong"))  # False
print("----------")

# find()
str5 = "Hi, welcome to my channel."
print(str5.find("welcome"))  # 4
print(str5.find("channel"))  # 18
print("")

# isalnum()
str6 = "alpha123"
print(str6.isalnum())  # True
print("")

# isdigit()
str7 = "812657"
print(str7.isdigit())  # True
str8 = "jaf1999"
print(str8.isdigit())  # False
print("----------")

# islower()
str9 = "all lowercase letters here."
print(str9.islower())  # True
str10 = "Not all LowerCASE letters here."
print(str10.islower())  # False
print("")

# isnumeric()
str11 = "6125498"
print(str11.isnumeric())  # True
str12 = "jaf1999"
print(str12.isnumeric())  # False
print("")

# isspace()
str13 = "   "
print(str13.isspace())  # True
print("----------")

# isupper()
str14 = "UPPER LETTERS"
print(str14.isupper())  # True
print("")

# partition()
str15 = "I can play chess anytime."
print(str15.partition("chess"))
