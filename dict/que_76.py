#Write a Python program to combine two lists into a dictionary. 
# The elements of the first one serve as keys and the elements of the second one serve as values.
# Each item in the first list must be unique and hashable.
a=['a', 'b', 'c', 'd', 'e', 'f']
b=[1, 2, 3, 4, 5]
c=dict(zip(a,b))
print(c)