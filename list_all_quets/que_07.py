#Write a Python program to remove duplicates from a list. 
a= input('input the list: ').split(',')
b=list(set(a))
print(sorted(b))