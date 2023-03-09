# Write a Python program to find the common values that appear in two given strings
a=set( input('the string: '))
b=set(input('the 2nd string: '))
common_chars = ""

for char in a:
    if char in b and char not in common_chars:
        common_chars += char

if common_chars == "":
    print("No common characters found!")
else:
    print("Common characters: " + common_chars)