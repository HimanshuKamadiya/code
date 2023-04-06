#Write a Python program to check if a given string contains an element that is present in a list.
def check(lst1,str1):
    for i in lst1:
        if i in str1:
            return True
a="https://www.w3resource.com/python-exercises/list/"
b= ['.com', '.edu', '.tv']
print(check(b,a))