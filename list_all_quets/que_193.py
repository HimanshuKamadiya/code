#Write a Python program to find the dimension of a given matrix
def dimension(lst):
    row=len(lst)
    col=len(lst[0])
    return row,col
a=[[1,2],[2,4]]
print(dimension(a))