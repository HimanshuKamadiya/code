#Write a Python program to sort a list of tuples using Lambda
a=input('the list of tuples: ')
l=tuple(a.sort(key=lambda x : x[1]))
print(l(a))