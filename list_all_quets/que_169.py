#Write a Python program to convert a given list of strings and characters to a single list of characters
def convert(lst):
    a=[i for words in lst  for i in words]
    return a
c=["red", "white", "a", "b", "black", "f"]
print(convert(c))