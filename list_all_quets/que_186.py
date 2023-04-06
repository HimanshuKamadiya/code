#Write a Python program to swap two sublists in a given list.
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
nums[6:10], nums[1:3] = nums[1:3], nums[6:10]
print(nums)