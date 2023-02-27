#.Write a Python program to find the first repeated word in a given string. 
a=input('the string: ')
count=0
b=a.split()
d={}
for i in b:
    if i in d:
      d[i]+=1
    print(i)
else:
    b[i]=1
   