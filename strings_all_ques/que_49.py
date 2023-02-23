# Write a Python program to count and display vowels in text.
text = input("Please enter some text: ")

vowels = 0

for char in text:
   # check whether the current character is vowel or not
   if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'
      or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
      vowels+=1
      print("Total number of vowels in the text: ", vowels,char)