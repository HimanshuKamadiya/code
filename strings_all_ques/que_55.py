#.Write a Python program to find the first repeated word in a given string. 
'''a=input('the string: ')
b=a.split()
d={}
for i in b:
    if i in d:
      d[i]+=1
print(i)'''
str = "Hello world ! Hello Tutor Joes"
t = set()
for txt in str.split():
	if txt in t:
	  print(txt)
	else:
	  t.add(txt)