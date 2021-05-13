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

                print(n.data,">>>>",end="")
                n=n.ref
    def add_at_begining(self,data):
        new_node = Node(data)
        new_node.ref = self.head

        self.head = new_node

    def add_at_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node

        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def inbetween_after(self,data,input):
        new_node=Node(data)
        n=self.head
        while n is not None:
            if n.data==input:
                new_node.ref=n.ref
                n.ref=new_node
                break
            n = n.ref
        if n is None:
            print(input,"node is not found in linked list")


    def inbetween_before(self, data, input):
        new_node=Node(data)
        n=self.head
        if self.head==None:
            print("Empty linked list")

        elif self.head.data==input:
            new_node.ref=self.head
            self.head=new_node
        else:
            while n is not None:
                if n.ref.data==input:
                    new_node.ref=n.ref
                    n.ref=new_node
                    break
                n=n.ref
l1=Linked_list()
l1.add_at_begining("kalluri")
l1.add_at_end("kumar")
l1.add_at_end("reddy")
l1.inbetween_after("siva","kalluri")
l1.inbetween_after(" hello i am new node after the kumar node ","kumar")
l1.inbetween_after("aaa","king")
l1.inbetween_before("king before","reddy")
l1.inbetween_before("hello before","siva")
l1.traverse()


