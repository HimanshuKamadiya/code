#Write a Python script to sort (ascending and descending) a dictionary by value
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
s=sorted(d.items(),key=lambda x:x[1])
print(s)
b=sorted(d.items(),key=lambda x: x[1],reverse=True)
print(b)