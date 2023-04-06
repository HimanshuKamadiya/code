# Write a Python program to append the same value/a list multiple times to a list/list-of-lists.
def add(n,m):
    c=[]
    c+=m*[n]
    return c
m=int(input('the char: '))
n=int(input('the timer: '))
print(add(m,n))