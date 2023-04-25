#Write a Python program to extract values from a given dictionary and create a list of lists from those values

def convert(dict,keys):
     return [list(d[k] for k in keys)for d in dict]
   
s = [
        {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
        {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
        {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
        {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
        {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
        ]
print(convert(s,('student_id','name','class')))
