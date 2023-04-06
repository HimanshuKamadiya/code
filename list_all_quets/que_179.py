#Write a Python program to create the largest possible number using the elements of a given list of positive integers.
from itertools import permutations

test_list = [3, 40, 41, 43, 74, 9]
res = int(max((''.join(i) for i in permutations(str(i)for i in test_list))))
print(res)