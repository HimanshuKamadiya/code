#Write a Python program to print the even numbers from a given list
def eve(lst):
    s=[i for i in lst if  i%2==0]
    return s
a=[1,2,3,4]
print(eve(a))