#Write a Python program to find the difference between two lists including duplicate elements.
def diff(lst1,lst2):
    c=[]
    for i in lst1:
        if i not in lst2 :
            c.append(i)
    return c
a=[1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
b=[1, 1, 2, 4, 5, 6]
print(diff(a,b))