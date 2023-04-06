# Write a Python program to split a given list into specified-sized chunks.
def chunks(lst,n):
    a=list((lst[i:i+n] for i in range(0, len(lst), n)))
    return a
b=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
n=int(input(': '))
print(chunks(b,n))