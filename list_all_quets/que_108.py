#Write a Python program to extract a specified column from a given nested list.
a=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
lst=[i.pop(0) for i in a]
print(lst)
