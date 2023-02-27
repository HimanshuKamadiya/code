#Write a Python program to find the first repeated character in a given string 
# where the index of the first occurrence is smallest.
a=input('the string: ')
d={}
y={}
for char  in a:
    k=d.keys()
    if char in k :
        y[char]=a.index(char)
    else:
        d[char] = a.index(char)
print(y)