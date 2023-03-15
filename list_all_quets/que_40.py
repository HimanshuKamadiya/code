# Write a Python program to split a list based on the first character of a word.
a=input('the list of word: ').split(',')
b=[]
for i in a:
    j=i[0]
    if j in b:
        b.append(i)
    print(j+":"+i)