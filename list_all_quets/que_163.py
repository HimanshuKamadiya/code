# Write a Python program to get the index of the first element that is greater than a specified element.
def first_el_index(a,n):
  return next(i[0] for i in enumerate(a) if i[1]>n)
a=[12,45,23,67,78,90,100,76,38,62,73,29,83]
m=int(input('the num: '))
print(first_el_index(a,m))