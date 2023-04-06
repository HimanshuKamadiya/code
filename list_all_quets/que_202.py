# Write a Python program to find the indexes of all None items in a given list.
def relative_order(lst):
    result = [i for i in range(len(lst)) if lst[i] == None]
    return result
a=[1, None, 5, 4, None, 0, None, None]
print(relative_order(a))