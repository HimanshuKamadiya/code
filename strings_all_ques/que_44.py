#Write a Python program to print the index of a character in a string. 
a=input('the string: ')
b=input('the character you want  index of: ')
for index in range(len(a)):
    if a[index]==b:# '==' is the comparison operater
        
        print('the index of {} is {}'.format(b, index))
    else:
        print("not available in the string ")