#Write a Python program to reverse words in a string.
a=input('the string: ')
b=a.split(' ')
l=[]
for i in b:
    l.append(i)

print(" ".join(l))