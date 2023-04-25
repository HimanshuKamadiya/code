#Write a Python program to combine two or more dictionaries, creating a list of values for each key
a={'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
b={'x': 300, 'y': 'Red', 'z': 600}

for i in b.keys():
    if i in a.keys():
        a[i]=[a[i], b[i]]
print(a)