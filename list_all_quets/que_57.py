#Write a Python program to check if all items in a given list of strings are equal to a given string
a=input('the string: ')
b=input('the list od strings: ').split()
for i in b:
    if len(a)==len(i):
        print('true')
    else:
        print('false')