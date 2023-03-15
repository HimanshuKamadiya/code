# initializing the main list
main_list = [1, 2, 3, 4, 5, 6]

# initializing the sublist
sub_list = [3, 4, 5]

# checking if sublist is present in main list
if all(elem in main_list for elem in sub_list):   # used all() in list comprehension
    
    print("Yes, the sublist exists in the main list")
else:
    print("No, the sublist does not exist in the main list")