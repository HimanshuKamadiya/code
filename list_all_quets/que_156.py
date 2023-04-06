#Write a Python program to add two given lists of different lengths, starting on the right.
def add(lst1,lst2):
    x=lst1[::-1]
    y=lst2[::-1]
    z=[]
    n=min(len(x),len(y))
    for i in range(n):
        t=x[i]+y[i]
        z.append(t)
    return z + x[n:] +y[n:]
b=[2, 4, 7, 0, 5, 8]
c=[3, 3, -1, 7]
print(add(b,c))