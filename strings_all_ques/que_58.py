#Write a Python program to move spaces to the front of a given string.
input_str = "  move spaces to the front"

# Initialize a variable to store the output string
output_str = ""

# Loop through each character in the input string
for char in input_str:

    # If the character is a space, add it to the beginning of the output string
    if char == " ":
        output_str = char + output_str

    # If the character is not a space, add it to the end of the output string
    else:
        output_str += char

# Print the output string
print(output_str)