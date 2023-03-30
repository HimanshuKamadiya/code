# Write a Python program to find common elements in a nested list.
a=[[12, 18, 23, 7, 25, 45], [7, 12, 18, 24, 28], [1, 5, 7, 8, 12, 15, 16, 18]]
c=[]
for i in range(len(a)):
    if i<len(a)-1:
        c.append(set(a[i]).intersection(a[i+1]))
for j in range(len(c)-1):
    print(set(c[j]).intersection(c[j+1]))