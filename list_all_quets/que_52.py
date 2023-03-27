a=input('the list1: ').split(',')
b=input('the list2: ').split(',')
c=[]
for i in a:
    if i not in b:
        c.append(i)
print(c)
d=[]
for j in b:
    if j not in a:
        d.append(j)
print(d)