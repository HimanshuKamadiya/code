#Write a Python program to move all zero digits to the end of a given list of numbers.
a=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
b=[]
c=[]
for  i in a:
    if i == 0:
        b.append(i)
    else:
        c.append(i)
print(b)
print(c)
print(c+b)