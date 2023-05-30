# Write a Python program to find if a given string starts with a given character using Lambda.
a=lambda x,y: True if x.startswith(y) else False
x='python'
y='p'
print(a(x,y))