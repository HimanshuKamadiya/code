#Write a Python program to find the last occurrence of a specified item in a given list.
def last_occ(a,chr):
    return ''.join(a).rindex(chr)
a=['s','d','f','s','d','f','s','f','k','o','p','i','w','e','k','c']
char=input('the char: ')
print(last_occ(a,char))