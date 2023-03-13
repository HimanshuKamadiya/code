# Write a Python function that takes two lists and returns True if they have at least one common member. 
a=input('the list1: ').split(',')
b=input('the list2: ').split(',')
c=[] # created a  emty string for add the common items from each string.
for i in a:
    for j in b:
        if i==j:
            c.append(i)
print('true, the list of common characters is',c)