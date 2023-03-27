#Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters.
a=[1, 1, 2, 3, 4, 4.3, 5, 1]
b={}
for i in a:
    k=b.keys()
    if i in k:
        b[i]+=1
    else:
        b[i]=1
keys=list(b.keys())
val=list(b.values())  
l=[]   
for i in range(len(keys)):
    l.append(str(keys[i]))
    l.append(str(val[i]))
print(''.join(l))