#Write a Python program to remove specific words from a given list.
def remove_word(a,b):
    c=[]
    for i in a:
        if i not in b:
            c.append(i)
    return  c
a=['red', 'green', 'blue', 'white', 'black', 'orange']
b=['white', 'orange']
print(remove_word(a,b))