#Write a Python program to find all the common characters in lexicographical order from two given lower case strings.
# If there are no similar letters print "No common characters".
a=input('the string1: ')
b=input('the string2: ')
char=''
for i in a:
    if i in b and i not in char :
        char+=i
if len(char)==0:
    print('no common letters')
else :
    print(sorted(char))