#Write a Python program to check if the elements of the first list are contained in the second one regardless of order.
def check(lst1,lst2):
    for i in lst1:
        if all(str(i)) in lst2:
            return True
        else:
            return False
a=[1, 2]
b=[2, 4]
print(check(a,b))