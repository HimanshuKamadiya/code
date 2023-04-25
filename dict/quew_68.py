#Write a Python program to combine two or more dictionaries, creating a list of values for each key. 
a={'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
b={'x': 300, 'y': 'Red', 'z': 600}
c={}
for i in a:
    if i in c:
        c[i].append(a[i])
    else:
        c[i]=[a[i]]
for i in b:
    if i in c:
        c[i].append(b[i])
    else:
        c[i]=[b[i]]
print(c)