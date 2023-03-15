#Write a Python program to print the numbers of a specified list after removing even numbers from it
a=input('the list of numbers: ')
b=[]
for i in a:
    if int(i) % 2 !=0:
        b.append(i)
print(b)