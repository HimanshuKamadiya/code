#Write a Python program to calculate the sum of the numbers in a list between the indices of a specified range.
def sum_nums(a,m,n):
    c=0
    for i in range(m,n+1):
        c+= i
    return c
a=[2,1,5,6,8,3,4,9,10,11,8,12]
m= int(input('the start of range: '))
n=int(input('the stop of the range'))
print(sum_nums(a,m,n))
