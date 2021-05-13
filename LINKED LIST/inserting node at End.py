class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linked_list:
    def __init__(self):
        self.head=None

    def traverse(self):

        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:

                print(n.data)
                n=n.ref
    def add_node(self,data):
        new_node = Node(data)
        if self.head==None:
            self.head=new_node

        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

l1=Linked_list()
l1.add_node("siva")
l1.add_node("kumar")
l1.traverse()


