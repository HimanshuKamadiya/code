#Write a Python program to convert more than one list to a nested dictionary
def nested(l1,l2,l3):
    r=[{x:{y:z}}for x,y,z in zip(l1,l2,l3)]
    return r
student_id = ["S001", "S002", "S003", "S004"] 
student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
student_grade = [85, 98, 89, 92]
print(nested(student_id,student_name,student_grade))