#Write a Python program to find the first non-repeating character in a given string.
a=input('user input string: ')
count=0
for char in a:
    if a.count(char)==1:
        print(char)