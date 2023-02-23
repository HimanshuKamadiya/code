# Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
a=input('the string name: ')
b=a[-1]+a[1:-1]+a[0]   # a[-1]=n,a[1:-1]= ytho, a[0]= p
print('the neww string: ',b)