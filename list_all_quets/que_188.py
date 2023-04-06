# Write a Python program to sort a given list of tuples by a specified element
def sort(lst,n):
    a= sorted(lst,key=lambda  x:x[n])
    return a

b=[('item2', 10, 10.12), ('item3', 15, 25.10), ('item1', 11, 24.50),('item4', 12, 22.50)]
n=int(input('the sorting point: '))
print(sort(b,n))