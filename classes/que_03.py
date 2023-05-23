# Write a Python program to create an instance of a specified class and display the namespace of the said instance.
class abc:
    def __init__(self,name,section):
        self.name=name
        self.section=section
c=abc('frank','b')
print(c.__dict__)