#Write a Python program to count the occurrences of each word in a given sentence.
a=input('enter the sentence: ')
#dict={} # Create a dictionary to store the word count
b=a.split(' ')
#b=list(a)
#print(b)
for i in b:
    print(i)
    c = b.count(i)
    print(i," : ",c)
    b.remove(i)
    