#Write a Python program to add a number to each element in a given list of numbers.
def add_each(lst,n):
   return [x+n for x in lst]
a=[3,8,9,4,5,0,5,0,3]
n=1
print(add_each(a,n))