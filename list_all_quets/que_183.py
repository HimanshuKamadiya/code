# Write a Python program to get the unique values in a given list of lists. 
def unique(lst):
    c=set(x for i in lst for x in i)
    return list(c)
b=[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
print(unique(b))
