# Write a Python program to count integers in a given mixed list.
a=[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
c=0
for i in a:
    if isinstance(i,int):
        c+=1
print(c)