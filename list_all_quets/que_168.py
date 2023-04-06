#Write a Python program to display vertically each element of a given list, list of lists. 
a=['a', 'b', 'c', 'd', 'e', 'f']
#Display each element vertically of the said list:
for i in a:
    print(i)
c=[[1, 2, 5], [4, 5, 8], [7, 3, 6]]
for a,b,d in zip(*c):
    print(a,b,d)