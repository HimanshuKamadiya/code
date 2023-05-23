#Write a Python program to execute a string containing Python code
a='''print('hello world')'''
exec(a)
b='''
def multy(a,b):
  return (a*b)
print(multy(2,3))'''
exec(b)