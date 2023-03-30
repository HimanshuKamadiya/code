# Write a Python program to find the item with the most occurrences in a given list.
a=['apple', 'banana', 'apple', 'orange', 'banana', 'pineapple', 'cherry', 'cherry', 'cherry']
c=None
b=0
for i in a:
    f=a.count(i)
    if f>=b:
        b=f
        c=i
print(b,i)