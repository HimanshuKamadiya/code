#Write a Python program to calculate the product of the unique numbers in a given list.
'''def abc(x):
    c=1
    c*=x
    return c
def  product_of_unique(a):
    b=[abc(x) for x in set(a)]
    return(b)
a = [10, 20, 30, 40, 20, 50, 60, 40]
print(product_of_unique(a))'''

def abc (x):
    c =1 
    for i in set(x):
        c*=i # for  multilying the  elements of thhee list: 
    return c
    
a = [10, 20, 30, 40, 20, 50, 60, 40]
print(abc(a))