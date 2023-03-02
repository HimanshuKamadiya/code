#. Write a Python program to find the second most repeated word in a given string
a= input('the string: ')
count={}
b=a.split()
#print(b)
for i in b:
    if i in count:
        count[i]+=1
        #print(i)
    else:
        count[i]=1
t = sorted(count.items())
print(t[-1])
