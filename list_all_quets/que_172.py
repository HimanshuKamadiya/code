#Write a Python program to remove the last N number of elements from a given list.
def remove_last_n(nums, N):
    result = nums[:len(nums)-N]
    return result    
nums = [2,3,9,8,2,0,39,84,2,2,34,2,34,5,3,5]
print("Original lists:")
print(nums)
N = 3

print(remove_last_n(nums, N))
N = 5

print(remove_last_n(nums, N))
N = 1

print(remove_last_n(nums, N))
