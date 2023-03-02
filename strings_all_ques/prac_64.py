##Write a Python program to find the maximum length of consecutive 0's in a given binary string
a=input('the sring: ')
count_0= 0
for char in a:
    if char=='0':
        count_0+=1