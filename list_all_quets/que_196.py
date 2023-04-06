#Write a Python program to move a specified element in a given list
def swap(lst,n,m):
    initial=lst[n]
    lasr=lst[m]
    lst[m]=initial
    lst[n]=lasr
    return lst
a=['red', 'green', 'white', 'black', 'orange']
n=int(input('index'))
m=int(input('the lasr: '))
#Move white at the end of the said list:
print(swap(a,n,m))