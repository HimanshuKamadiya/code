#A Python dictionary contains List as a value. 
# Write a Python program to clear the list values in the said dictionary
a={ 
               'C1' : [10,20,30], 
               'C2' : [20,30,40],
               'C3' : [12,34]
             }
for i in a:
    a[i].clear()
print(a)