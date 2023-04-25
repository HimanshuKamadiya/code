#Write a Python program to multiply all the items in a dictionary.
a={'data1':100,'data2':-54,'data3':247}
c=1
for i in a:
    c*=a[i]
print(c)