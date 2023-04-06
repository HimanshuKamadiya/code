# Write a Python program to find common elements in a given list of lists
def common(lst): 
  res =[set.intersection(*map(set, lst))]
  return res
a=[[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]
print(common(a))
