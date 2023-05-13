class node:
    def __init__(self,value):
        self.head=value
        self.next=None
class listt:
    def __init__(self) -> None:
        self.h=None
    def printl(self):
       ps=self.h
       while ps is not None:
           print(ps.head)
           ps=ps.next
l=listt()
l.h=node(1)
s=node(2)
t=node(3)
l.h.next=s
s.next=t
l.printl()