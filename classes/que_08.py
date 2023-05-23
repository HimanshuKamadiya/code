#Write a Python program to create two empty classes, Student and Marks.
# Now create some instances and check whether they are instances of the said classes or not.
# Also, check whether the said classes are subclasses of the built-in object class or not.
class student:
    pass
class marks:
    pass
student1=student()
student2=student()
marks1=marks()
marks2=marks()
print(isinstance(student1,student))
print(isinstance(student2,marks))
print(isinstance(marks1,marks))
print(isinstance(marks2,student))