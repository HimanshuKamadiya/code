#Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
a= 'The lyrics is not that poor!'
b=a.find('not')
c=a.find('poor')# find gives the index of 1st element of the string. 
if b<c:
    print(a[0:b]+'good.')
