#. Write a Python program to pack consecutive duplicates of a given list of elements into sublists
import itertools

my_list = [1, 1, 2, 3, 3, 3, 4, 4, 5, 6, 6]

packed_list = [list(x) for m, x in itertools.groupby(my_list)]
print(packed_list)
