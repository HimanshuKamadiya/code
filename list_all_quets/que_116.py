#Write a Python program to sort a list of lists by a given index of the inner list.
def sorted_list_list(lst,index):
    return sorted(lst,key=lambda x:x[index])
lst=[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
index=int(input('the num of index: '))
print(sorted_list_list(lst,index))