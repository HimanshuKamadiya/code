#Write a Python program to find repeated items in a tuple
a=(1, 2, 3, 2, 4, 5, 5, 6, 6)
c=[]
for i in a:
    if a.count(i)>1:
        if i not in c:
          c.append(i)
print(c)