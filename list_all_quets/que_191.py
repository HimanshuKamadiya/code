#Write a Python program to find the maximum and minimum values of the three given lists.
def max_min(lst1,lst2,lst3):
    return max(lst1+lst2+lst3),min(lst1+lst2+lst3)
nums1 = [2,3,5,8,7,2,3]
nums2 = [4,3,9,0,4,3,9]
nums3 = [2,1,5,6,5,5,4]
print(max_min(nums1,nums2,nums3))