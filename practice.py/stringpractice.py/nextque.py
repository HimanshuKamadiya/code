#Write a Python program that accepts a filename from the user and prints the extension of the file.
a= input("Enter the file name : ")
ext=a.split(".")
print(ext)
print("the file extension is: " ,ext[-1])