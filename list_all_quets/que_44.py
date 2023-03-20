#Write a Python program to generate groups of five consecutive numbers in a list
#n=int(input("Enter the number : "))
l =[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5 ,10,12,33,15]
o =[]
for i in range(0,len(l),5):
    m=[]
    for j in range(i, i+5):
        m.append(l[j])
    o.append(m)
print(o)

