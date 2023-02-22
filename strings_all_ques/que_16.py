#Write a Python function to insert a string in the middle of a string.
a=input('the string namme: ')
c=input('the string namme: ')
b=int(len(a)/2)
print(a[:b]+c+a[b:])