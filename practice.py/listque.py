#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
s1="abc"
s2="xyz"
n1=s1[:2]+s2[2:]
n2=s2[:2]+s1[2:]
print("the new string",n1)