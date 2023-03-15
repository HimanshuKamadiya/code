#Write a Python program to insert an element before each element of a list
a=[1,2,3,4,5]
b='*'
c=[]
for i in a:
    c.append(b)
    c.append(i)
print(c)