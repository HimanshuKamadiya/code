#Write a Python program to convert a given list of lists to a dictionary.
def convert(lst):
      a= {i[0]:i[1:] for i in lst}
      return a
b=[[1, 'Jean Castro', 'V'], 
   [2, 'Lula Powell', 'V'], 
   [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'],
   [5, 'Zachary Simon', 'VII']]
print(convert(b))
