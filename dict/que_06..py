#Write a Python script to generate and print a
# dictionary that contains a number (between 1 and n) in the form (x, x*x).
d={}
n= int(input('the num: '))
for i in range(1,n+1):
    d[i]=i*i
print(d)