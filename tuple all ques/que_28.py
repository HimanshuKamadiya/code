#Write a Python program to convert a tuple of string values to a tuple of integer values. 
a=(('333', '33'), ('1416', '55'))
b=tuple((int(i[0]),int(i[1])) for i in a)
print(b)