#Write a Python program to join two given list of lists of the same length, element wise.
def join(lst1,lst2):
    a=[x+y for x,y in zip(lst1,lst2)]
    return a
b=[[10,20], [30,40], [50,60], [30,20,80]]
c=[['p','q'], ['p','s','t'], ['u','v','w']]
print(join(b,c))