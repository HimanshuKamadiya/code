#Write a Python program to extract every first or specified element from a given two-dimensional list.
def extract(a,c):
    b=[x[c]for x in a]
    return b
c=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
n=int(input('the num: '))
print(extract(c,n))