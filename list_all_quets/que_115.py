# Write a Python program to check if the elements of a given list are unique or not
def unique(lst):
    if len(lst)>len(set(lst)):
        return False
    return True
a=[1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
print(unique(a))
b=[2, 4, 6, 8, 10, 12, 14]
print(unique(b))