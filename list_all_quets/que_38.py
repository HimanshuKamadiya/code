#Write a Python program to change the position of every n-th value to the (n+1)th in a list. 
a=input('the main list: ').split(',')
for i in range(0,len(a),2):
    a[i],a[i+1]=a[i+1],a[i]
print(a)