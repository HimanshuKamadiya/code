#. Write a Python program to extract numbers from a given string.
a= input('the string: ')
b=''
for i in a:
    if i.isdigit():
        b+=i
print(b)