#Write a Python function student_data () that will print the ID of a student (student_id).
# If the user passes an argument student_name or student_class the function will print the student name and class.
def student_data(student_id,student_name=None,student_class=None):
    print(f'Student_id:{student_id}')
    if student_name and student_class is not None:
        print(f'Student_class:{student_class}')
        print(student_name)
student_data(1234)
student_data(1234,'john',2)
