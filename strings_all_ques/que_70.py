##Write a Python program that concatenates uncommon characters from two strings.
a=input('the string1: ')
b=input('the string2: ')
c=''
for i in a:
    if i not in b:
        c+=i    
print(c)