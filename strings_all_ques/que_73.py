#Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.
a=input('the string: ')
upper=0
lowercase=0
numeric=0
special_char=0
for char in a:
    if char.isupper():
        upper+=1
    elif char.islower():
        lowercase=+1
    elif char.isnumeric():
        numeric+=1
    else:
        special_char+=1
print(upper)
print(lowercase)
print(numeric)
print(special_char)
