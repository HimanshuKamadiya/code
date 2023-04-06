#Write a Python program to find the common tuples between two given lists.
def find_common(lst1,lst2):
    c=[]
    for i in lst1:
        if i in lst2:
            c.append(i)
    return c
a=[('red', 'green'), ('black', 'white'), ('orange', 'pink')]
b=[('red', 'green'), ('orange', 'pink')]
print(find_common(a,b))