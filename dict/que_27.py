#Write a Python program to convert a list into a nested dictionary of keys
def convert(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return {lst[0]: convert(lst[1:])}
my_list = ['a', 'b', 'c', 'd']
my_dict = convert(my_list)
print(my_dict)
