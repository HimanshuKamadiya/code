#Write a Python function to convert a given string to all uppercase 
# if it contains at least 2 uppercase characters in the first 4 characters.
a=input('the string name: ')
count=0 #to start the count
for i in a[:4]:
    if i.upper() == i:
        count+=1
if count>=2:
    print(a.upper())
else:
    print(a)