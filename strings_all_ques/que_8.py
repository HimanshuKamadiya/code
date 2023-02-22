#Write a Python function that takes a list of words and return the longest word and the length of the longest one.
l=["PHP", "Exercises", "Backend"]

if len(l[0])> len(l[1]) and len(l[0]) > len(l[2]):
    print(" largest: ", l[0], len(l[0]))
elif len(l[1])>len(l[2]):
    print("Largest", l[1], len(l[1]))
else:
    print("Largest", l[2], len(l[2]))