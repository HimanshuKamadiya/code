# Write a Python program to count the number of elements in a list within a specified range. 
a=input('the list: ').split(',')
b=input('lowest num: ')
c=input('highest num')
d=len(list(i for i in a if b <= i <= c))# TypeError: object of type 'generator'# has no len()) when print without changing it in to the list.
print(d)