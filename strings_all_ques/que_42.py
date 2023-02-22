#Write a python program to count repeated characters in a string. 
a=input('the string: ')
d={}
for i in a:
    k=d.keys()
    if i in k:
        d[i]+=1
    else:
        d[i]=1
print(d)