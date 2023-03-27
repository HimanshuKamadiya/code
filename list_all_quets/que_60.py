#Write a Python program to find a tuple, the smallest second index value from a list of tuples. 
def find_the_smallest_index_value(a):
    c=[]
    for i in a:
        if i[1]<i[0]:
         c.append(i)  
    return c  
a=input('the lis off tuples: ').split()
result= find_the_smallest_index_value(a)

print(result)