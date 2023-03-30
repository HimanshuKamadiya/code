# Write a Python program to sort a given list of strings(numbers) numerically.
def sort(a):
   d=[int(i) for i in a]
   d.sort()
   return d
b= ['4','12','45','7','0','100','200','-12','-500']
print(sort(b))