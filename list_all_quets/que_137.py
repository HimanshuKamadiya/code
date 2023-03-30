# Write a Python program to find the first even and odd number in a given list of numbers. 
def  remove(lst):
    even=[i for i in a if i%2==0]
    odd=[i for i in a if 1%2!=0]
    return even[0],odd[0]
    
a=[1,3,5,7,4,1,6,8]
print(remove(a))