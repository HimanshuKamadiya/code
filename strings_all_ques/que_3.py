# Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
a= input('the string name :')
b=a[0:2]+a[-2:]
if  len(a)<=2 : #the length of string 'a'
    print(' ')
else:
    print(b)
