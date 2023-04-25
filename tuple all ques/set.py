#Write a Python program to find all the anagrams and group them together 
# from a given list of strings. Use the Python data type
def anagram(lst):
    c=[i for i in lst if all(i) in next(i)]
    return c
a= ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(anagram(a))
