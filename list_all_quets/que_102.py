# Write a Python program to extract specified size of strings from a give list of string values
a=['Python', 'list', 'exercises', 'practice', 'solution']
n=8
ext=[]
for i in a:
    if len(i)==n:
        ext.append(i)
print(ext)