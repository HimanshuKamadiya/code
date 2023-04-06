#Write a Python program to convert a given list of tuples to a list of lists
def convert(a):
    return [list(i) for i in a]
b= [(1, 2), (2, 3), (3, 4)]
print(convert(b))
