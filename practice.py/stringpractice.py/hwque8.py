#Write a Python function that takes a list of words and return the longest word and the length of the longest one.
a=input('user input:')
b=input('user input:')
c=input('user input:')
l=[a,b,c]

if len(a)>len(b)>len(c):
    print('the longest word',a,len(a))
elif len(b)>len(a)>len(c):
    print('the longest word',b,len(b))
elif len(c)>len(a)>len(b):
    print('the longest word',c,len(c))