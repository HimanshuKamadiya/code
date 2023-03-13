#Write a Python program to add two strings as if they were numbers (positive integer values). Return a message if the numbers are strings.
a=input('the string: ')
b=input('the second sttring: ')
if a.isdigit() and b.isdigit():
    c=str(int(a)+int(b))
print(c)