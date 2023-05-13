class node():
    def __init__(self,value):
        self.head=value
        self.next=None
        print()
class lisst:
    def __init__(self):
        self.h=None
    def printl(self):
        ps=self.h
        while ps is not None:
           print(ps.head)
           ps=ps.next  
l=lisst()
l.h=node('mon')
s=node('tue')
t=node('wed')
l.h.next=s
s.next=t
l.printl()
