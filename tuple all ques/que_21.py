#Write a Python program to replace the last value of tuples in a list.
a=[(1, 2, 3), (4, 5, 6), (7, 8, 9)]
b=[i[:-1]+(10,) for i in a]
print(b)