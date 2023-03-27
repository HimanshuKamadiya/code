# Write a Python program to check whether all dictionaries in a list are empty or not.
a= [{1:2},{},{}]
for i in a:
    if i =={}:
        print('true')
    else:
        print('false')