#Write a Python program to find missing and additional values in two lists
a=input('the list1: ').split(',')
b=input('the list2: ').split(',')
c=[]
for i in a:
    if i not in b:
        c.append(i)
print('the diffrence for list 1 ',c)
d=[]
for j in b:
    if j not in a:
        d.append(j)
print('the difference in list 2: ',d)