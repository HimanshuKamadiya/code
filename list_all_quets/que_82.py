# Write a Python program to generate combinations of n distinct objects taken from the elements of a given list
import itertools
a=input('the list: ').split()
c=list(itertools.combinations(a,3))
print(c)