# Define a Python function student(). Using function attributes display the names of all arguments.
def student(name,age):
    print(f'Name: {name}')
    print(f'Age: {age}')
print(student.__code__.co_varnames)