class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linked_list:
    def __init__(self):
        self.head=None
    def add_node(self,data):
        if self.head==None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Linked is not empty")
    def traverse(self):
        if self.head==None:
            print("Empty Linked list")
        else:
            print(self.head.data)
l1=Linked_list()
l1.add_node("siva")
l1.add_node("kumar")
l1.traverse()
