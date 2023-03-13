#Write a Python program to remove punctuation from a given string
import string

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

# testing!
sample_input = "Hello, my name is John. I'm excited to learn Python!"
print("Punctuation removed String: ", remove_punctuation(sample_input))