# Write a Python program to sum a specific column of a list in a given list of lists
def sum_col(a,b):
    b=sum(i[b] for i in a)
    return b
c= [
        [1,2,3,2],
        [4,5,6,2],
        [7,8,9,5],
        ]
d=int(input('the col num: '))
print(sum_col(c,d))