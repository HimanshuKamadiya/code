#Write a Python program to remove the nth index character from a nonempty string. 
a=input('the user input:')
b= int(input('the user input:'))
c=a[:b]+a[b+1:]
print(c)
