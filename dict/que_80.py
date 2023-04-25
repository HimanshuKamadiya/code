#Write a Python program to find the key of the maximum value in a dictionary.
def maxi(d):
    return max(d,key=d.get),min(d,key=d.get)
a={'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
print(maxi(a))
