# Write a Python program to check if there are duplicate values in a given flat list.
def check(lst):
    if  len(lst)!=len(set(lst)):
        return True
    else:
        return False
a=[1, 2, 3, 4, 5, 6, 7]
b=[1, 2, 3, 3, 4, 5, 5, 6, 7]
print(check(a))
print(check(b))