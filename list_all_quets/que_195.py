#Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
color = ["red", "green", "white", "black"]
for i, el in reversed(list(enumerate(color))):
    print(i, el) 