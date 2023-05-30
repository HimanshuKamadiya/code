#Write a Python program to create a function that takes one argument, 
# and that argument will be multiplied with an unknown given number.
def compute(n):
   return lambda x: x*n
n=int(input('the num: '))
x=int(input('the multiple num: '))
a=compute(n)
print(a(x))