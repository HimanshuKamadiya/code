#Write a Python program to square 
# and cube every number in a given list of integers using Lambda.
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=list(map(lambda x:x**2,a))
c=list(map(lambda x: x**3,a))
print(b)
print(c)