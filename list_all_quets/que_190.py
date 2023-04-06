# Write a Python program to find the specified number of largest products from two given lists, multiplying an element from each list.
def largest_products(list1, list2, n):
    '''products = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            products.append(list1[i] * list2[j])
    products.sort(reverse=True)
    return products[:n]'''
    result = sorted([x*y for x in nums1 for y in nums2], reverse=True)[:n]
    return result

nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [3, 6, 8, 9, 10, 6]
n=int(input('the size of output: '))
print(largest_products(nums1,nums2,n))