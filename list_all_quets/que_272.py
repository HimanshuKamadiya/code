 #Generates a list of numbers in the arithmetic progression within a range
def gen(a,b):
    return list(range(a,b-1,a))
print(gen(1,15))