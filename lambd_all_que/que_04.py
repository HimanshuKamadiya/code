# Write a Python program to sort a list of dictionaries using Lambda.
a=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print(sorted(a,key=lambda x: x['color']))