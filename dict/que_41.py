#Write a Python program to drop empty items from a given dictionary.
a={'c1': 'Red', 'c2': 'Green', 'c3': None}
b={key:value for key,value in a.items() if value is not None}
print(b)