#Write a Python program to convert a given list of strings into a list of lists.
def convert(lst):
    c=[[i]for i in lst]
    return c
a=['Red', 'Maroon', 'Yellow', 'Olive']
print(convert(a))
  
