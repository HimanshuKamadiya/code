# Write a Python program to insert an element in a given list after every nth position.
def insert_nth(lst, val, n):
    new_list = []
    for i in range(len(lst)):
        if i % n == 0 and i != 0:
            new_list.append(val)
        new_list.append(lst[i])
    return new_list

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_val = 0
nth_pos = 3

new_list = insert_nth(my_list, new_val, nth_pos)
print(new_list)
