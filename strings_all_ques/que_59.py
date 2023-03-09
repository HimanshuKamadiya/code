#Write a Python program to find the maximum number of characters in a given string.
'''a = "hello","world"
b = max(a)
print(b,len(b))'''

'''new solution'''
a=input('the string: ')
b=a.split()
c=''
for i in b:
    c=max(b)# for saving i in c.
print(c,len(c))
