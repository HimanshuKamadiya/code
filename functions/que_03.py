#Write a Python function to multiply all the numbers in a list
def muly(lst):
    t=1
    for i in lst:
        t*=i
    return t
a=(8, 2, 3, -1, 7)
print(muly(a))