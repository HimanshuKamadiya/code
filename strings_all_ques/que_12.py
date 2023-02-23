#Write a Python program to count the occurrences of each word in a given sentence.
a=input('enter the sentence: ')
count={}
words=a.split()
for word in words:
    if word in count:
        count[word]+=1
    else :
        count[word]=1
print(count)
