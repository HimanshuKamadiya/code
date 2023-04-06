#Write a Python program to convert a Unicode list to a list of strings
def convert(lst):
    a=[str(x) for x in lst]
    return a
b=['S001', 'S002', 'S003', 'S004']
print(type(b))
print(convert(b))