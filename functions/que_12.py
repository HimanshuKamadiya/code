# Write a Python function that checks whether a passed string is a palindrome or not.
def check(strg):
   if strg==strg[::-1]:
     print(True)
   else:
        print(False)
check('aza')
    
    