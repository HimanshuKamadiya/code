#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

n = input("Enter a numner : ") # n is the string
# we need the equantion n+nn+nnn
a= n
b= n+n
c= n+n+n
#print(int(n)+int(n+n)+int(n+n+n))
print(a,b,c)
d = int(a)+int(b)+int(c)
print("The solution of the equation is : ",d)