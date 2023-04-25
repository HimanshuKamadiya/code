#Write a Python program to remove a specified dictionary from a given list.
test_list = [{"id" : 1, "data" : "HappY"},
             {"id" : 2, "data" : "BirthDaY"},
             {"id" : 3, "data" : "Rash"}]
a=[i for i in test_list if  (i['id']!=2)]
print(a)