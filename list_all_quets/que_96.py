#Write a Python program to sort a given list of lists by length and value.
a=[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
a.sort(key=lambda i:(len(i),i))
print(a)