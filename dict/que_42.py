#Write a Python program to filter a dictionary based on value
marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
a={k:v for k,v in marks.items() if v>=170}
print(a)