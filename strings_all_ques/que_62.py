# Write a Python program to compute the sum of the digits in a given string.
a=input('enter the string: ')
total=0
for char in a:
    if char.isdigit():# Check if the current character is a digit
        int_char = int(char)
        
        # Add the Integer Representation of the Current Character to the Running Total
        total += int_char
print(total)