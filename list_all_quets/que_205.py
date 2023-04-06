#Write a Python program to find the indices of elements in a given list that are greater than a
def search(lst,n):
    a=[i for i,el in enumerate(lst) if el>=n]
    return a
b=[1234, 1522, 1984, 19372, 1000, 2342, 7626]
n=int(input('the um of compaarision: '))
print(search(b,n))
#Indices of elements of the said list, greater than 3000