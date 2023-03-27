#write a Python program to select the odd items from a list.
a=input('the list: ').split(',')
b=[]
for i in a:
    if int(i)%2== 1:
        b.append(i)
print(b)