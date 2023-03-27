#Write a Python program to sort a list of nested dictionaries.
a=[{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}] 
a.sort(key=lambda e:e ['key']['subkey'])
print(a)