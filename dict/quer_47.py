# Write a Python program to split a given dictionary of lists into lists of dictionaries.
a={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
#B=[{keys:value[i] for keys,value in a.items()}for i in range(len(a['science']))]
#print(B)
original_dict = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35], 'gender': ['female', 'male', 'male']}

list_of_dicts = [{key: value[i] for key, value in original_dict.items()} for i in range(len(original_dict['name']))]

print(list_of_dicts)
