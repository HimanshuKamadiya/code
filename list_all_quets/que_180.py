#Write a Python program to create the smallest possible number using the elements of a given list of positive integers.
from itertools import permutations
def smallest(lst):
    a=int(min(''.join(i) for i in permutations(str(i)for i in lst)))
    return a
b=[3, 40, 41, 43, 74, 9]
print(smallest(b))