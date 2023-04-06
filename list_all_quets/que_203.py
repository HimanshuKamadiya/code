# Write a Python program to join adjacent members of a given list.
def join_(lst):
    a=[[lst[i]+lst[i+1]] for i in range(len(lst)-1)][::2]
    return a
b= ['1','2','3','4','5','6','7','8']
print(join_(b))
