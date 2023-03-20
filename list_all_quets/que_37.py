# Write a Python program to find common items in two lists.
a=input('the list1: ').split(',')
b=input('the list2: ').split(',')
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)

