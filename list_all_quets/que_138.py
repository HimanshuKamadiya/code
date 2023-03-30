#Write a Python program to sort a given mixed list of integers and strings. Numbers must be sorted before strings.
def sort(lst):
    integer=sorted([i for i in lst if type(i) is int])
    string=sorted([i for i in lst if type(i) is str])
    return integer+string
a=[19,'red',12,'green','blue', 10,'white','green',1]
print(sort(a))