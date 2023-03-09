#Write a Python program to remove leadingaddress zeros from an IP .
a=input('the ip address: ')
b=a.split('.')#Split the IP address into seperate and created a list
c=[] # Create empty list to store non-zero b
for i in b:# Iterate through each i, if the i is not 0, store in c list
    #for j in i:
     #   if j !='0':
      #      c.append(j)
    if i[0:2] =='00':
        c+=i[2]+"."
    elif i[0]=='0':
        c+=i[1:]+"."
    else:
        c+=i+"."
c.pop(-1)       
print(''.join(c))

'''import re

# enter the IP address here
ip_address = "000.120.098.054" 

# Remove leading zeros
new_ip = re.sub('\.[0]*', '.', ip_address)

print("IP address with leading zeros removed:", new_ip)'''