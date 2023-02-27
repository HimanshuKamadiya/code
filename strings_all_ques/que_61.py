#Write a Python program to remove duplicate characters from a given string.
a=input('the string: ')
b=[]
for char in a:
    if char in b:
        b[char]