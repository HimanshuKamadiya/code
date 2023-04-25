#Write a Python program to find the length of a dictionary of values.
a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
v={}
for i in a.values():
   v[i]=len(i) 
print(v)
