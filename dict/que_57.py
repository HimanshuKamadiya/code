#Write a Python program to filter even numbers from a dictionary of values. 
def test(dict):
    a={key:[value for value in values if value%2==0]for key,values in dict.items()}
    return a
dict={'V' : [1, 4, 6, 10], 'VI' : [1, 4, 12], 'VII' : [1, 3, 8]} 
print(test(dict))

