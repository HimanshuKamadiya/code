#Write a Python program to generate a number in a 
# specified range except for some specific numbers.
import random
def gen(start,stop,num):
    b=random.choice([i for i in range(start,stop+1)if i not in num])
    return b
num=[1,5,7]
start=int(input('the start'))
stop= int(input('the stop: '))
print(gen(start,stop,num))