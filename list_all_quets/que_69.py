#Write a Python program to remove duplicates from a list of lists.
A=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]] 
b=[]
for i in A:
    if i not in b:
        b.append(i)
print(b)