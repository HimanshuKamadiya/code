# Write a Python program to remove the None value from a given list.
def remove(lst):
    for i in lst:
        if i == None:
            lst.remove(i)
    return lst
a=[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
print(remove(a))