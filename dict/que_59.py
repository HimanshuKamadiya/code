#Write a Python program to find the specified number of maximum values in a given dictionary.
def test(dict,n):
    a=sorted(dict,key=dict.get,reverse=True)[:n]
    return a
dictt = {'a':5, 'b':14, 'c': 32, 'd':35, 'e':24, 'f': 100, 'g':57, 'h':8, 'i': 100}
n=5
print(test(dictt,n))