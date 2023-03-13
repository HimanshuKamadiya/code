#Write a Python program to count the number of strings from a given list of strings. 
# The string length is 2 or more and the first and last characters are the same.
a=input('the list of string: ').split()
b=0
for i in a:
    if len(i)>=2 and i[0]==i[-1]:
        b+=1
print(b)