#Write a Python program to find the maximum and minimum values in a given list of tuples.
def abc(lst):
    a=max(lst,key=lambda x: x[1])
    b=min(lst,key= lambda x:[1])
    return a,b
b= [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
print(abc(b))