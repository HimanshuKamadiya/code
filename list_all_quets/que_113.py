#Write a Python program to remove duplicate dictionary entries from a given list.
a=[{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
n=[]
for i in a:
    if i not in n:
        n.append(i)
print(n)