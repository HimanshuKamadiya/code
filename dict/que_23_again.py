#Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
a= [{'item': 'a', 'amount': 400}, {'item': 'b', 'amount': 300}, {'item': 'a', 'amount': 750}]
d={}
for i in a:
    if i['item'] not in d.keys():
        d[i['item']]=i['amount']
    else:
        d[i['item']]+=i['amount']
print(d)