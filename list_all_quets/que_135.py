#Write a Python program to iterate over all pairs of consecutive items in a given list. 
def iterate_consecutive_pairs(lst):
    return list(zip(lst[:-1], lst[1:]))

my_list = [1, 2, 3, 4, 5]
print(iterate_consecutive_pairs(my_list))
