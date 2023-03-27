#Write a Python program to split a list every Nth element
a=input('the list : ').split(',')
c=int(input('the number: '))
b=[]
for i in range(0,len(a),c):
    b.append(a[i:i+c])
print(b)