#Write a Python program to print all permutations with a given repetition 
# number of characters of a given string. 

from itertools import permutations
a=input('the string: ')
b=int(input('the number: '))
l=permutations(a,b)
for i in l:
    print(l)
    