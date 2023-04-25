#Write a Python program to print all distinct values in a dictionary.
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
d=set(val for i in L for val in i.values())
print(d)