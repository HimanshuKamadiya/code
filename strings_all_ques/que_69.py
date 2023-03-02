#Write a Python program to find the longest common sub-string from two given strings
a=input('the string1: ')
b=input('the string2: ')
for i in range(len(a),len(b)):
    if(a[i]==b[i]):
        print(i)