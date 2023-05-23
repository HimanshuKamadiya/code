#Write a Python class named Student with two instances student1, student2 and 
# assign values to the instances' attributes. Print all the attributes of the student1, student2 instances
# with their values in the given format.
class student:
    pass
student1=student()
student1.student_id='12345'
student1.student_name='amit'
student2=student()
student2.student_id = "V12"
student2.marks_language = 85
student2.marks_science = 93
student2.marks_math = 95
for i,j in student1.__dict__.items():
    print(f"{i} : {j}")
print(' ')
for i,j in student2.__dict__.items():
    print(f"{i}:{j}")