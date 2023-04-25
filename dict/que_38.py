#Write a Python program to match key values in two dictionaries.
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
common=set(x.keys()) and set(y.keys())
for i in common:
    if x[i]==y[i]:
        print('true',i)
    else:
        print('false',i)