#Write a Python program to insert a given string at the beginning of all items in a list.
'''def insert(a,string):
    for i in a:
        return string+ str(i)
a= [1,2,3,4]
string='emp'
c=insert(a,string)
print(c)'''
num = [1,2,3,4]
print(['emp{0}'.format(i) for i in  num])