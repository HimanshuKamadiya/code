#Write a Python program to compute the sum of all the elements of 
# each tuple stored inside a list of tuples.
def  compute(a):
    b=[x+y for x,y in a ]
    return b
a=[(1, 2), (2, 3), (3, 4)]
print(compute(a))