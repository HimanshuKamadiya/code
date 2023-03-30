#Write a Python program to check if a substring appears in a given list of string values. 
def check_sub(sub,string_list):
    for i in string_list:
        if sub in i:
            return True
    return False
a=['red', 'black', 'white', 'green', 'orange']
b='him'
print(check_sub(b,a))