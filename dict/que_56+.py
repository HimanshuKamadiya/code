#Write a Python program to convert a dictionary into a list of lists
a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
b=[[keys,value] for keys,value in a.items()]
print(b)