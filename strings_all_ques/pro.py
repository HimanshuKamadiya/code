#for words

a=input(" enter the string : ")
x = input("Enter the string : ")
b=a.split(" ")
y=x.split(" ")
c=[] # common words
for i in b:
    if i in y:
        c.append(i)
print(" ".join(c))