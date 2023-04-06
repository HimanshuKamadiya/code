# Write a Python program to interleave lists of varying lengths.
def interleave(x,y,z):
    c=min(len(x),len(y),len(z))
    u=[]
    for i in range(c):
        u.append(x[i])
        u.append(y[i])
        u.append(z[i])
    return u+x[c:]+y[c:]+z[c:]
a=[2, 4, 7, 0, 5, 8]
b=[2, 5, 8]
d=[2, 5, 8]
print(interleave(a,b,d))