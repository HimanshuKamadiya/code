#Write a Python program to Zip two given lists of lists
# Define two lists of lists
list1 = [[1, 2], [3, 4], [5, 6]]
list2 = [['a','b'], ['c', 'd'], ['e', 'f']]

# Zip the lists together
zipped_lists = list(map(list.__add__,list1, list2))

# Print the resulting zipped list
print("Zipped Lists:", zipped_lists)
