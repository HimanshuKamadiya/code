# Write a Python program to flatten a given nested list structure.
a= [[20, 30],[60, 70, 80], [90, 100, 110, 120]]
b=[]
for i in a:
    for j in i:
        b.append(j)
print(b)