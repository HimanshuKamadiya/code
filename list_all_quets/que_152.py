#Write a Python program to combine two sorted lists using the heapq module. 
from heapq import merge
a=[1, 3, 5, 7, 9, 11]
b=[0, 2, 4, 6, 8, 10]
print(list(merge(a,b)))