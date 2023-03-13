#Write a Python program to find the list of words that are longer than n from a given list of words
a=input('the list of words: ').split(' ')
b=input('the nth word: ')
c=[]
for i in a:
    if len(i)> len(b):
        c.append(i)
print(c)