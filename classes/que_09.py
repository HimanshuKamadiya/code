#Write a Python class named Student with two attributes student_name, marks.
# Modify the attribute values of the said class and print the original and modified values of the said attributes.
class student:
    def __init__(self,name,marks):
        self.student_mname=name
        self.student_marks=marks
    def pp(self):
        print(f'student name: ',self.student_mname)
        print(f'marks : ',self.student_marks)
obje=student('john',90)
obj=student('priya',25)
obje.pp()
obj.pp()