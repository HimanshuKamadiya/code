#Write a Python program that accepts a hyphen-separated sequence of words as input 
# and 
# prints the words in a hyphen-separated sequence after sorting them alphabetically.
a=input('the data: ')
s=[i for i in a.split('-')]
s.sort()
print('-'.join(s))