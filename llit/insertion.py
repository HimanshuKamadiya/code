class node:
    def __init__(self,value):
        self.head=value
        self.next=None
class llist:
    def __init__(self):
        self.h=None
    def printt(self):
        ps=self.h
        while ps is not None:
            print(ps.head)
            ps=ps.next
    def atbegining(self,newdata):
        newnode=node(newdata)
        #update the links
        newnode.next=self.h
        self.h=newnode
    def delete(self, dele):
        a=self.h
        if a != None:
            while(a):
                if a.head == dele:
                    break
                p = a
                a = a.next
            if a == None:
                return
            p.next=a.next
            a=None
l=llist()
l.h=node('1')
c=node('2') 
e=node('3')
l.h.next=c
c.next=e
new = node(4)
e.next = new
l.atbegining('0')
l.printt()
l.delete('2')
l.printt()
