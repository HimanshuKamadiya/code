# Write a Python function to sum all the numbers in a list. 
def summ(lst):
    return sum(i for i in lst)
a=(8, 2, 3, -1, 7)
print(summ(a))