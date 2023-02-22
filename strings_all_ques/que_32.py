# Write a Python program to print the following 
# positive and negative numbers with no decimal places. 
a= input("enter a float : ")
c = a.split(".")
print(c[0]+c[1][0:])