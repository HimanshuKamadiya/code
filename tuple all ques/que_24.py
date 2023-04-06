#Write a Python program to count the elements in a list until an element is a tuple
a=[10,20,30,(10,20),40]
c=0
for i in a:
    if isinstance(i,tuple):
        break
    c+=1
print(c)