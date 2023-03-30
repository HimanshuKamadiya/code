#Write a Python program to check whether a specified list is sorted or not.
def is_sorted(list):
    for i in range(1,len(list)):
        if list[i]<list[i-1]:
            return False
    return True
a=[1, 2, 3, 4, 5]
b=[1, 3, 2, 4, 5]
print(is_sorted(a))
print(is_sorted(b))
