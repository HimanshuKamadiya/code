#Write a Python program to find items starting with a specific character from a list.
a= input('the list: ').split(',')
b=[]
for i in a:
    if i.startswith('h'):
        b.append(i)
print(b)