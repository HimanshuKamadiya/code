class node:
    def __init__(self,value):
        self.head=value
        self.next=None
class llinked_list:
    def __init__(self):
        self.h=None
    def p_print(self):
        ps=self.h
        while ps is not None:
            print(ps.head)
            ps=ps.next
    def at_start(self,new_data):   #adding data at start.
        new_node=node(new_data)
        new_node.next=self.h # updating the list.
        self.h=new_node     # assign the self.h of llist to new_node.
    def Inbetween(self,middle_node,newdata):
      if middle_node is not None:
         NewNode = node(newdata)
         NewNode.next = middle_node.next
         middle_node.next = NewNode
    def remove_node(self,target_node_data):
        if self.head is not None:
            if self.head.data == target_node_data:
                self.head=self.head.next
l=llinked_list()
l.h=node('1')
c=node('2')
e=node('3')
l.h.next=c
c.next=e
e.next=node('4')#at last
l.at_start('0')
l.Inbetween(l.h.next,"Fri")
l.p_print()