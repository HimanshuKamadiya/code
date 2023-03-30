#. Write a Python program to find the maximum and minimum product of pairs of tuples within a given list
def max_val_tuple(lst):
    max=max([x*y for x,y in lst])
    min=min([x*y for x,y in lst])
    return max,min
a=[(2, 7), (2, 6), (1, 8), (4, 9)]
print(max(a))
print(min(a))