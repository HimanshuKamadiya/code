#Write a Python program to iterate over two lists simultaneously
a=input('the list1: ').split(',')
b=input('the list2: ').split(',')
x=zip(a,b)
print(x)