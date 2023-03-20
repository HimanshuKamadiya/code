#Write a Python program to generate groups of five consecutive numbers in a list
a=input('the list: ').split(',')
b=[]
for i in range(0,len(a),5):
    c=[]
    for j in range(i,i+5):
        c.append(a[j])
    b.append(c)
print('the list of 5 consecutive numbers: ',b)



