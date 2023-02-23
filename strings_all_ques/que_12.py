#Write a Python program to count the occurrences of each word in a given sentence.
a=input('enter the sentence: ')
count={}
words=a.split()
for i in words:
    if i in count:
        count[i]+=1
    else :
        count[i]=1
print(count)
