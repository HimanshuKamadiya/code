#Write a Python program to check if two lists have the same elements in them in same order or not.
def same_pos_same_element(lst1,lst2):
    for i in range(len(lst1)):
        if lst1[i]!=lst2[i] :
            return False
    return True
a=[1, 2, 3, 4, 5]
b=[1, 2, 3, 4, 5]
c= [1, 2, 3, 5, 4]
print(same_pos_same_element(a,b))
print(same_pos_same_element(a,c))