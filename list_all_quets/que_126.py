#Write a Python program to interleave multiple lists of the same length.
def interleave(x,y,z):
    c=[]
    for i in zip(x,y,z):
        if len(x)==len(y)==len(z):
            for j in i:
                c.append(j)
    return c
a= [1, 2, 3, 4, 5, 6, 7]
b= [10, 20, 30, 40, 50, 60, 70]
c= [100, 200, 300, 400, 500, 600, 700]
#print([[j for j in i] for i in interleave(a,b,c)])
print(interleave(a,b,c))
