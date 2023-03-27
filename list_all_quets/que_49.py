#Write a Python program to convert a list to a list of dictionaries.
name= ["Black", "Red", "Maroon", "Yellow"]
code=["#000000", "#FF0000", "#800000", "#FFFF00"]
a={name:code for name,code in zip(name,code)}
print(a)