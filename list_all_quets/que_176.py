#Write a Python program to create a new list by dividing two given lists of numbers.
def divide(lst1,lst2):
    return [x/y for x,y in zip (lst1,lst2)]
nums1 = [7,2,3,4,9,2,3]
nums2 = [9,8,2,3,3,1,2]
print(divide(nums1,nums2))