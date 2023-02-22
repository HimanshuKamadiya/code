#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged..
def add_suffix(a):
  if len(a) < 3:
    return a # english return??
  elif a[-3:] == 'ing':#why -3
    return a + 'ly'
  else:
    return a + 'ing'

print(add_suffix("strxfrg"))
print(add_suffix("string"))
print(add_suffix('ab'))