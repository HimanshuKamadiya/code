#Write a Python program to convert a given string to Snake case
a=input('the string1: ')
b=[]
for i in a:
    if i.upper()==i and a.index(i)>0:
       b+='_'+i
       
    else:
        b+=i
print("".join(b))