#Write a Python program to remove sublists from a given list of lists that contain an element outside a given range
a=[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]

low = 5
high = 12

new_lst = [sublst for sublst in a if all(low <= x <= high for x in sublst)]
print(new_lst)
