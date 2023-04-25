#Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
from itertools import product
d= {'1': ['a', 'b'], '2': ['c', 'd']}
for i in product(*[d[k]for k in d.keys()]):
    print(''.join(i))