#Write a Python program to get the total length of all values in a given dictionary with string values
def sum_len_val(dict):
    r=sum(len(value) for value in dict.values())
    return r
a={'#FF0000':'Red', '#800000':'Maroon', '#FFFF00':'Yellow', '#808000':'Olive'}
print(sum_len_val(a))