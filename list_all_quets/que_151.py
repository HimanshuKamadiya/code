#Write a Python program to find the maximum and minimum values in a given list within a specified index rangedef
def find_max_min(a,m,n):
    c=max(i for i in range(m,n+1) if i in a)
    d=min(i for i in range(m,n+1) if i in a)
    return c,d
a=[4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
m=int(input('the m: '))
n=int(input('the n: '))
print(find_max_min(a,m,n))