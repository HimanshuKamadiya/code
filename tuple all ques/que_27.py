# Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
def product(tup):
    return[sum(x)/len(x) for x in tup]
    #return [sum(x)/len(x) for x in zip(*tup)]
a=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print(product(a))
