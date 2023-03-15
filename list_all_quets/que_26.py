#Write a Python program to check whether two lists are circularly identical.
a=input('th list: ')
b= input('the list: ')
if len(a)==len(b) and a in b:
    print('true they are identical')
else:
    print('false they are not idenntical')