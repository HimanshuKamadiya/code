# Write a Python program to remove the first specified number of elements from a given list satisfying a condition.
def remove_first_n_even_numbers(lst, n):
    count = 0
    i = 0
    while i < len(lst) and count < n:
        if lst[i] % 2 == 0:
            lst.pop(i)
            count += 1
        else:
            i += 1
    return lst

my_list = [2, 4, 6, 8, 10, 11, 12, 14, 16, 18]
n=int(input(': '))
result = remove_first_n_even_numbers(my_list, n)
print(result)
