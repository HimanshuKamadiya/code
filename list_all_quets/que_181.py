#Write a Python program to iterate a given list cyclically at a specific index position.
def cyclically(lst,i):
    c=lst[i:]
    d=lst[:i]
    return c+d
a= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
from_=3
print(cyclically(a,from_))