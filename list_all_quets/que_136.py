# Write a Python program to remove duplicate words from a given list of strings
'''def remove(lst):
    return list(set(lst))
a=['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
print(remove(a))'''
def remove(lst):
    l=[]
    for i in lst:
        if i not in l:
            l.append(i)
    return l
a=['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
print(remove(a))