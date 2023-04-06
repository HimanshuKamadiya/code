#Write a Python program to concatenate element-wise three given lists.
def concatinate(l1,l2,l3):
    a=[x+c+v for x,c,v in zip(l1,l2,l3)]
    return  a
c= ['0','1','2','3','4'] 
d = ['red','green','black','blue','white']
e = ['100','200','300','400','500'] 
print(concatinate(c,d,e))