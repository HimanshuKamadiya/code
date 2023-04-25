#Write a Python program to replace dictionary values with their sums. 
def average(dic):
    for i in dic:
        a1=i.pop('V')
        a2=i.pop('VI')
        i['V+VI']=(a1 + a2)/2
    return dic
student_details= [
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]
print(average(student_details))
