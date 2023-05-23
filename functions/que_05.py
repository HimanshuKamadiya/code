#Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument
def fac(n):
    a =1
    for i in range(1,n+1): #stop excluded 
        a*=i
    print(a)

n = int(input("Enter a number : "))
fac(n)