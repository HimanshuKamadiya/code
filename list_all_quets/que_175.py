#Write a Python program to find the minimum and maximum value for each tuple position in a given list of tuples.
def find(lst):
    zip(*lst)
    r1=map(max,zip(*lst))
    r2=map(min,zip(*lst))
    return list(r1),list(r2)
a= [(2,3),(2,4),(0,6),(7,1)]
print(find(a))
