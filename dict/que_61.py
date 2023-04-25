#Write a Python program to count the frequency of a dictionary.
from collections import Counter
def test(dict):
    a=Counter(dict.values())
    return a
b= {
 'V': 10,
 'VI': 10,
 'VII': 40,
 'VIII': 20,
 'IX': 70,
 'X': 80,
 'XI': 40,
 'XII': 20, 
 }
print(test(b))