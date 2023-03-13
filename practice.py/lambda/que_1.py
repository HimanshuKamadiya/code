#Write a Python program to create a lambda function that adds 15 
# to a given number passed in as an argument, 
# also create a lambda function that multiplies 
# argument x with argument y and prints the result.
a=int(input('the string: '))
l=lambda i: i+15
print(l(a))
a= lambda i,y:i*y
print(a(12,4))