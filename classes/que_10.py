#Write a Python class named Student with two attributes student_id, student_name.
# Add a new attribute student_class and display the entire attribute and the values of the class.
# Now remove the student_name attribute and display the entire attribute with values.
class student:
    def __init__ (self,student_id, student_name):
        self.student_id=student_id
        self.student_name=student_name
s=student(12345,'amit')
s.studnet_clas='10'
for i,j in  s.__dict__.items():
    print(f"{i}:{j}")
print('after deletion: ')
del s.student_name
for i,j in s.__dict__.items():
    print(f"{i}:{j}")
    