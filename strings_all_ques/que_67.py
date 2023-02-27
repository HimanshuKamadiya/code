#Write a Python program to remove all consecutive duplicates of a given string.
a=input('the string: ')  
in_l= list(a)
b=[]
for char in in_l:
    if char not in  b or b[-1]!= char:#For each character in the list, if the result list is empty
        #or the last character doesn't match with the current one then append it to the result list.
        b.append(char)
print('.'.join(b)) #convert the filtered list back into a string