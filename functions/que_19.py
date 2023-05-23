#Write a Python program to access a function inside a function.
def outer():
    s='himanshu'
    def inner():
        print(s)
    inner()
outer()