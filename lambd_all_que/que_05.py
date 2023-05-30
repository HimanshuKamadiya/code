# Write a Python program to filter a list of integers using Lambda.
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b= [list(filter(lambda x: x%2==0,a))]
print(b)
c=list(filter(lambda x: x%2!=0,a))
print(c)