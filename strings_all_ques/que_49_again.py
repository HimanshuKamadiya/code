 #Write a Python program to count and display vowels in text.
a=input("the namme of the strig: ")
count= 0
for char in a:
    if(char =='a'or char=='i' or char=='o' or char=='u' or char =='e'
       or char=='A'or char =='I' or char=='O'or char=='U' or char=='E'):
        count+=1
    print('the count of the vowels  in the string is ',count,char)