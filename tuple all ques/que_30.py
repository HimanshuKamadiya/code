#Write a Python program to check if a specified element appears in a tuple of tuples
def check(tup,c):
    #a=any(c in el for el in tup)
    a= any(c in [j for j in i]for i in tup)
    return a
b=(('Red', 'White', 'Blue'),
    ('Green', 'Pink', 'Purple'),
    ('Orange', 'Yellow', 'Lime'),)
c='White'
print(check(b,c))