#Write a Python program to get items from a given list with specific conditions.
#Number of Items of the said list which are even and greater than 45.
def count(lst):
    c=0
    for i in lst:
        if i%2==0 and i>45:
            c+=1
    return c
a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
print(count(a))