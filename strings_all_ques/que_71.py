#Write a Python program to move all spaces to the front of a given string in a single traversal.
a=input('the string: ')
b=a.split()
for char in a:
    if char == ' ':
        b=a.replace(' ','')
print(char+b)