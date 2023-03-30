def remove_list(a):
    b=[]
    c=[i for i in a if i !=b]
    return c
a=[[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
print(remove_list(a))