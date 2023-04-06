#Write a Python program to convert a given decimal number to a binary list.
def convert_binary(n):
    a=[int(x) for x in list('{0:0b}'.format(n))]
    return a
b=8
print(convert_binary(b))