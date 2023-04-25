#Write a Python program to get all combinations of key-value pairs in a given dictionary
from itertools import combinations
def test(dict1):
    a=list(map(dict,combinations(dict1.items(),2)))
    return a
p={'V' : [1, 4, 6, 10], 'VI' : [1, 4, 12], 'VII' : [1, 3, 8]}
print(test(p))
