# Write a Python program to check whether the n-th element exists in a given list. 
n=input('the nth elemnet: ')
a=input('the list: ').split(',')
for i in a:
    if i==n:
        print('true')
    else:
        print('false')
   