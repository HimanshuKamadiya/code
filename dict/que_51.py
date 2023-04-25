#A Python Dictionary contains List as a value. 
# Write a Python program to update the list values in the said dictionary
dict = {'a': [1, 2, 3], 'b': [4, 5], 'c': [6, 7, 8, 9]}
dict['a'][1]=20
dict['b'].append(97)
dict['c'].extend([11,12])
print(dict)