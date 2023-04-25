# Write a Python program to transform a dictionary into a list of tuples
a={'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
c=list((key,value)for key,value in a.items())
print(c)