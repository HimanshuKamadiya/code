# Write a Python program to detect the number of local variables declared in a function.
def abcc():
    a=1
    c=2
    s=3
    b='w3resources'
print(abcc.__code__.co_nlocals)