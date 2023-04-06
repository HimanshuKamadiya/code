# Write a Python program to pair consecutive elements of a given list.
def consecturtive_pair(lst):
    return[[lst[i],lst[i+1]]for i in range(0,len(lst)-1,2)]
a= [1,2,3,4,5,6]
print(consecturtive_pair(a))