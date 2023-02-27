#Write a Python program to remove leading zeros from an IP address.
a=input('the ip address: ')
b=a.split('.')#Split the IP address into seperate and created a list
c=[]# Create empty list to store non-zero b
for i in b:# Iterate through each i, if the i is not 0, store in new_octets list
    if i !='0':
        c.append(i)
print('.'.join(c))