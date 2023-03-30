# Write a Python program to remove all elements from a given list that are present in another list.
a= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=[2, 4, 6, 8]
for i in a:
    if i in b:
        a.remove(i)
print(a)