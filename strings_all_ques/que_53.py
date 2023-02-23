#Write a Python program to find the first repeated character in a given string.
a=input('the string: ')
count=0
for char in a:
    if a.count(char)==2:
        print(char)