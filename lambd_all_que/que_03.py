# Write a Python program to sort a list of tuples using Lambda.
a=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
a.sort(key= lambda x:x[1])
print(a)