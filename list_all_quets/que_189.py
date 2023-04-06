#Write a Python program to shift last element to first position and first element to last position in a given list. 
def shift_first_last(lst):
        first_elem = lst[0]
        last_elem = lst[-1]
        lst[0] = last_elem
        lst[-1] = first_elem
        return lst
lst = [1, 2, 3, 4, 5]
print(shift_first_last(lst))
