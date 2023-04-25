# Write a Python program to find the shortest list of values for the keys in a given dictionary.
a= {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]} 
b=[keys for keys, value in a.items() if len(value)==1]
print(b)