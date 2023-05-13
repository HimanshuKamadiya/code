#Write a Python function that accepts a string and
#counts the number of upper and lower case letters.
#
def check(s):
    d=0
    c=0
    for i in s:
        if i.isupper():
            d+=1
        elif i.islower():
            c+=1
        else:
            pass
    return (d,c)
a='The quick Brown Fox'
print(check(a))
        