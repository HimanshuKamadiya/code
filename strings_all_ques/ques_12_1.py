#Write a Python program to count the occurrences of each word in a given sentence.

a = input("Enter a string : ")
b = a.split(" ") # converting the string in list 
d = {}
for i in b : 
    k = d.keys()
    if i in k: # to check if the '
        if i in k:
          d[i]+=1
    else: 
        d[i]=1
print(d)