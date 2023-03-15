#tke out the prime number from the user input range:
a=int(input('the last num of range: '))
non=[]
prime=[]
for  i in range(2,a+1):
    if i not in prime:
        prime.append(i)
        for j in range(i*i,a+1,i):
            non.append(j)
print(prime)