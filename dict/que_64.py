#Write a Python program that creates key-value list pairings within a dictionary.
from itertools import product
def create(dictt):
    a=[dict(zip(dictt,i))for i in product(*dictt.values())]
    return a
s = {1: ['Jean Castro'], 
2: ['Lula Powell'], 
3: ['Brian Howell'], 
4: ['Lynne Foster'], 
5: ['Zachary Simon']}
print(create(s))