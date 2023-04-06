#Write a Python program to convert a given list of tuples to a list of strings.
def convert(lst):
  c=[str(i[0])+' '+i[1] for i in lst]
  return c
a=[('red', 'green',), ('black', 'white'), ('orange', 'pink')]
print(convert(a))