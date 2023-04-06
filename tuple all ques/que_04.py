#Write a Python program to unpack a tuple into several variables
a=1,2,3
b=tuple(a)
c,d,e=b
print(c)
print(d)
print(e)
print(c,d,e)