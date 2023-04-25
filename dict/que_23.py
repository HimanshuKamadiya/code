#Write a Python program to combine values in a list of dictionaries.
a= [{'item': 'a', 'amount': 400}, {'item': 'b', 'amount': 300}, {'item': 'a', 'amount': 750}]
b={}
for i in a : # to read the list
    if i['item'] in b.keys():
        b[i['item']]+= i['amount']
    else:
        b[i["item"]]=i["amount"]
print(b)