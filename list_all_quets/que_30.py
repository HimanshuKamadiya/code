#Write a Python program to get the frequency of elements in a list.
import collections
a=input('the list: ').split(',')
print(collections.Counter(a))