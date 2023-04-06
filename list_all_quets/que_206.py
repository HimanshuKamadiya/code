#Write a Python program to remove additional spaces from a given list.
def remove_extra_space(lst):
    c=[]
    for i in lst:
        j=i.replace(' ','')
        c.append(j)
    return c

a=['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy']
print(remove_extra_space(a))