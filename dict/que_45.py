#Write a Python program to create a dictionary grouping a sequence of 
# key-value pairs into a dictionary of lists
a=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
c={}
for key,value in a:
    if key in c:
        c[key].append(value)
    else:
        c[key]=[value]
print(c)