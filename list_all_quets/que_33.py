#Write a Python program to generate all sublists of a lis
lst = [1, 2, 3, 4]
sublists = []
for i in range(len(lst)):
    for j in range(i+1, len(lst)+1):# why i +1?
        
        sublists.append(lst[i:j])# slicing by loop variable

print(sublists)
