# Write a Python program to generate and print a list of the first and last 5 elements 
# where the values are square numbers between 1 and 30 (both included)
def printValues():
	l = list()
	for i in range(1,30):
		l.append(i**2)
	print(l[:5]+l[-5:])

printValues()