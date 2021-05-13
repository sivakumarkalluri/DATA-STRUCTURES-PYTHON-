class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linked_list:
    def __init__(self):
        self.head=None
    def traverse(self):
        n=self.head
        while n is not None:
            print(n.data)
            n=n.ref
    def add_node(self,data):
        new_node=Node(data)
        n=self.head
        if n==None:
            self.head=new_node
        else:
            while n.ref is not None:
                n=n.ref

            n.ref=new_node
    def delete_first_node(self):
        n=self.head
        if self.head.ref==None:
            self.head=None
        else:
            self.head=n.ref
    def delete_last_node(self):
        n=self.head
        if self.head.ref==None:
            self.head=None
        else:
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def delete_inbetween(self,input):
        if self.head==None:
            print("Empty Linked list")
        elif self.head.data==input:
            self.head=None
        else:
            n=self.head
            while n.ref.data is not input:
                n=n.ref
            n.ref=n.ref.ref


l1=Linked_list()
l1.add_node("kalluri")
l1.add_node("siva")
l1.add_node("kumar")
l1.add_node("Reddy")
l1.add_node("hello")
l1.delete_first_node()
l1.delete_last_node()
l1.delete_inbetween("kumar")
l1.traverse()
