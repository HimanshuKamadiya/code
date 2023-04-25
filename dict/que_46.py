#Write a Python program to split a given dictionary of lists into lists of dictionaries.
test_dict = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# using zip()
# to convert dictionary of list to
# list of dictionaries
a=[dict(zip(test_dict,i))for i in zip(test_dict.values())]
print(a)
