#Write a Python program to remove a specific item from a given list of lists.
def remove(lst):
    a=[i[1:] for i in lst]
    return a
b=[['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
print(remove(b))