#Write a Python function to check whether a string is a pangram or not.
def pnagram(input_tring):
    alpha='abcdefghijklmnpqrstuvwxyz'
    for i in alpha:
        if i not in input_tring.lower():
            return False
        else:
            return True
a=input('str: ')
print(pnagram(a))