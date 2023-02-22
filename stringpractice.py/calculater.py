a=int(input('the numbers: '))
b=int(input('the numbers: '))
c=int(input('Press 1 for Add, 2 for Sub, 3 for Mul, 4 for Div : '))
if c == 1 : 
    print("sum : ", a+b)
elif c == 2 : 
    print("Diff : ", a-b)
elif c == 3 : 
    print("Mul : ",a*b)
elif c==4 : 
    print("Div : ", a/b)
else: 
    print("Invalid Choice!!")