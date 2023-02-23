#Write a Python program to remove the nth index character from a nonempty string.
a=input('the string name: ')
b=int(input('the nth index: '))
c=a[:b]+a[b+1:] #stop is always excluded.
print ('the string output: ',c)
