#Write a Python function that takes a number as a parameter and 
#checks whether the number is prime or not.
def check(a):
    for i in range(2,a):
        if a%i==0:
            return False
        else:
            return True
a=9
print(check(a))