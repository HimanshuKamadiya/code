#. Write a Python function to get a string made of the first three characters of a specified string. 
# If the length of the string is less than 3, return the original string.
a=input('the string name: ')
if len(a)<3:
    print(a)
else:
    print(a[:3])