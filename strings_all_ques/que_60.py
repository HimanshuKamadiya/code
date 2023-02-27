#Write a Python program to capitalize the first and last letters of each word in a given string.
a=input("the string: ")
b=a.split()
for i in b:
    b[[i]]+=i[0].upper()+i[1:-1]+i[-1].upper
