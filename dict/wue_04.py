#Write a Python script to check whether a given key already exists in a dictionary
a={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
b=int(input('the int: '))
if b in a.keys():
    print('true')
else:
    print('false')