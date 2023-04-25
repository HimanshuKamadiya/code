#Write a Python program to convert a list of dictionaries into a list of values corresponding to the specified key.
def convert(lst,key):
    return[i.get(key)for i in lst]
     
students = [
  { 'name': 'Theodore', 'age': 18 },
  { 'name': 'Mathew', 'age': 22 },
  { 'name': 'Roxanne', 'age': 20 },
  { 'name': 'David', 'age': 18 }
]
print(convert(students,'name'))