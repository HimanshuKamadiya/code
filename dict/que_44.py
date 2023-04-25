# Write a Python program to filter the height and width of students, which are stored in a dictionary.
def filter(a):
    b={c:d for c,d in a.items() if d[0]>=6 and d[1]>=70}
    return b
students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
print(filter(students))