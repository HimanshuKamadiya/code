##Write a Python program that concatenates uncommon characters from two strings.
a=input('the string1: ')
b=input('the string2: ')
c=()
for i in range(len(a),len(b)):
    if (a[i]!= b[i]):
        c.add(a[i])
        c.add(b[i])
print(c)
