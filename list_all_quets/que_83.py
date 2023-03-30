# Write a Python program to round every number in a given list of numbers and print the total sum multiplied by the length of the list
a=[22.4,4.0,-16.22,-9.1,11.0,-12.22,14.2,-5.2,17.5]
b=[]
for i in a:
    b.append(int(abs(i)))
print(b)
sum=0
for i in b:
    sum+=1
print(sum*len(a))