# Write a Python program to calculate the difference between the two lists.
a=input('the list1: ')
b=input('the list2: ')
c=[]
for i in a:
    if i not in b:
        c.append(i)
print(c)