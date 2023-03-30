#Write a Python program to count the number of sublists that contain a particular element.
a=[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
c=0
for i in a:
    for j in i:
        if j in i:
            c+=1
    print(c)