#Write a Python program to compute the sum of digits of each number in a given list.
def sum_of_digits(lst):
    return [sum(int(digit)for digit in str(j))for j in lst]
a=[12,21,3]
print(sum_of_digits(a))