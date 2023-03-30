#Write a Python program to reverse strings in a given list of string values
def reverse(lst):
    return [x[::-1]for x in lst]


a=["Red", "Green", "Blue", "White", "Black"]
print(reverse(a))