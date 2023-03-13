#Write a Python program to check whether
# any word in a given string contains duplicate characters or not.
a=input('input the string: ')
b=a.split()
for i in b:
    if len(a)!=len(b):
      print('true')
    else:
        print('false')
