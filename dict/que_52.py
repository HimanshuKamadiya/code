#Write a Python program to extract a list of values from a given list of dictionaries.
dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]
c=[i['b']for i in dicts]
print(c)