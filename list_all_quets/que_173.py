# Write a Python program to merge some list items in a given list using the index value.
def merge(lst,_from,_to):
    result=lst
    result[_from:_to] = [''.join(lst[_from:_to])]
    return result

a= ['a', 'b', 'c', 'd', 'e', 'f', 'g']
c=int(input('_from: '))
d=int(input('_to: '))
print(merge(a,c,d))