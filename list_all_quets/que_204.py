#Write a Python program to check if the first digit or character of each element in a list is the same
def check_first_character(lst):
    first_char = str(lst[0])[0]  
    for i in range(1, len(lst)):
        if str(lst[i])[0] != first_char:
            return False
    return True
my_list = [1234, 122, 1984, 19372, 100]
print(check_first_character(my_list)) 