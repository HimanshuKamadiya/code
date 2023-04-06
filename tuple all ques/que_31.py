#Write a Python program to compute the element-wise sum of given tuples.
a=(1, 2, 3, 4)
b=(3, 5, 2, 1)
c=(2, 2, 3, 1)
print(tuple(map(sum,zip(a,b,c))))