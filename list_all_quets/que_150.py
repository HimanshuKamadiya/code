#Write a Python program to reverse a given list of lists.
def reverse(a):
    return a[::-1]
b=[['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
print(reverse(b))