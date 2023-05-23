#Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class.
# Create a function to display all attributes and their values in the Student class.
class student:
    def __init__(self,student_id,student_name):
        self.student_id=student_id
        self.student_name=student_name
s=student(12345,'amit')
s.student_class='python'
for i,j in s.__dict__.items():
    print(f"{i} : {j}")