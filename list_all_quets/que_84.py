#Write a Python program to round the numbers in a given list, 
# print the minimum and maximum numbers and multiply the numbers by 5. 
# Print the unique numbers in ascending order separated by space.
a=[22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
b=[]

for i in a:
        b.append(int(abs(i)))
print('the round numbers: ',b)
maximum=max(b)
minmum=min(b)
print('largest number: ',maximum)
print('smallest numbers: ',minmum)
c=[]
for i in b:
    c.append(i*5)
print('the round number multiples: ',c)
print('the unique list: ',sorted(a))