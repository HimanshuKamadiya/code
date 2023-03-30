#Write a Python program to count the number of lists in a given list of lists.
a=[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
c=0
for i in a:
   for j in i:
      if j in i:
         c+=1
print(c)