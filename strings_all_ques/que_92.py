#Write a Python program to find string similarity between two given strings
a=input('the string: ')
b=input(' the 2nd string: ')
c=[]
for i in a:
    if i in b:
        c.append(i)
else:
    print('no similar items')
print(c)