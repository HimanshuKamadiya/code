#Write a Python program to add two given lists of different lengths, starting on the left
def add(lst1,lst2):
    a=[int(x)+int(y) for x,y in zip(lst1,lst2)]
    return a
b=[2, 4, 7, 0, 5, 8]
c=[3, 3, -1, 7]
print(add(b,c))