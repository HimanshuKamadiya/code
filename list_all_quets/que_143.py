#Write a Python program to get the frequency of elements in a given list of lists.
def find_freq(a):
    c={}
    for sub in a:
        for i in sub:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
    return c
b=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
print(find_freq(b))
