# Write a Python program to remove all strings from a given list of tuples.
def remove_str(lst):
    result =   [tuple(v for v in i if not isinstance(v, str)) for i in lst]
    return result
a=[(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
print(remove_str(a))