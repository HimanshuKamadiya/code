#Write a Python program to remove an empty tuple(s) from a list of tuples.
a=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
b=[]
for i in a:
    if i !=():
        b.append(i)
print(b)
c=[i for i in a if i]
print(c)