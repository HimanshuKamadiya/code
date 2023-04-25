#Write a Python program to create a dictionary from two lists without losing duplicate values
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]
a=dict(zip(test_keys,test_values))
print(str(a))