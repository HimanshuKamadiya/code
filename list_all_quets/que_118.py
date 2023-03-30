#Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeric values
def find_diff(lst):
    return [lst[n+1]-lst[n] for n in range(len(lst)-1)]
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_diff(a))