#Write a Python program to get every nth element in a given list.
def get(lst,nth):
    a=[lst[nth-1::nth]]
    return a
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nth=int(input('the nth el'))
print(get(b,nth))