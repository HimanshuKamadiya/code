#Write a Python program that accepts a filename from the user and prints the extension of the file.

f_n = input("Enter the file name : ")
ext = f_n.split(".")
print(ext)
print("the required file extension is : ", ext[-1])