#Write a Python program to determine the index of a given string at which a certain substring starts. 
# If the substring is not found in the given string return 'Not found'
a=input('the main string: ')
b=input('the sub string: ')
if b in a:
    print(f"the string{b} in the index of {a.index(b)}" )
else:
    print('not found')