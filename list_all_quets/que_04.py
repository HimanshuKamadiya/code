#Write a Python program to get the smallest number from a list
a=input('the list: ')
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(sorted(b)[0])