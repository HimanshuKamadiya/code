#Write a Python program to reverse each list in a given list of lists.
def reverse(a):
    b=[[i[::-1]] for i in a]
    return b
a=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(reverse(a))
