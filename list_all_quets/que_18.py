#Write a Python program to generate all permutations of a list in Python
import itertools
a=input('the list: ').split(',')
print(list(itertools.permutations(a)))