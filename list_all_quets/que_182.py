#Write a Python program to calculate the maximum and minimum sum of a sublist in a given list of lists.
def sum_(lst):
    a=max(lst,key=sum)
    c=min(lst,key=sum)
    return a,c
a=[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
print('max: ',sum_(a)[0])
print('min: ',sum_(a)[1])