#Write a Python program to find all the common characters in lexicographical order from two given lower 
# case strings.
# If there are no similar letters print "No common characters".
a=input('the string 1: ')
b=input('the string 2: ')
c=[]
for i in a:
    if i in b:
        c+=i
print(sorted(c))