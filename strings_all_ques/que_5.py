# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
a= input('the string name: ')
b= input('the second string name: ')
c=b[0:2]+a[-1]+" "+a[0:2]+b[-1]
print(c)