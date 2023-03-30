#Write a Python program to compute average of two given lists. 
a=[1, 1, 3, 4, 4, 5, 6, 7]
b=[0, 1, 2, 3, 4, 4, 5, 7, 8]
def average(lst):
    return sum(lst)/len(lst)
avg1=average(a)
avg2=average(b)
final_avg=(avg1+avg2)/2
print(final_avg)
