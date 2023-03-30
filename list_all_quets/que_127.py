#Write a Python program to remove words from a given list of strings containing a character or string.
def remove_word(a,b):
   for i in list(a):
       for j in b:
           if j in i:
               a.remove(j)
       return a
a=['Red color', 'Orange#', 'Green', 'Orange @', 'White']
b=['#', 'color', '@']
print(remove_word(a,b))