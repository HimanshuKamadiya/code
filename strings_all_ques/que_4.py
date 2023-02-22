#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. 
a=input('the name of string:')
b=a[0]
c=a.replace(b,'$')
d=b+c[1:]
print(d)