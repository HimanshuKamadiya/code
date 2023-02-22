#Write a Python program to count the number of characters (character frequency) in a string.
a=input('the user intput:')
d={}
for i in a:
    print(i)
    k=d.keys() # list where all the keys of 'd' is save.
    print(k)
    if i in k:
        d[i]+=1
        print("in if", d)
    else :
      d[i]=1
      print("in else", d)
print(d)