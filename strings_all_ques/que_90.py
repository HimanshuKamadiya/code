#Write a Python program to remove duplicate words from a given string
a=input('the string: ')
b=a.split()
c=[]
for i in b:
    if i not in c:
        c.append(i)
print(" ".join(c))