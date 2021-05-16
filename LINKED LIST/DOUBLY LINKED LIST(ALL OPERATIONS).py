class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class Linked_list:
    def __init__(self):
        self.head=None
    def add_front(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head==None:
            self.head=new_node
        elif self.head.nref==None:
            new_node.pref=self.head
            self.head.nref=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            new_node.pref=n.pref.nref
            n.nref=new_node

    def forward_traverse(self):
        if self.head==None:
            print("Linked list is empty")
        else:
            print(">>>>>>>>>>>>>>>> Forward Traversing")
            n=self.head
            while n is not None:
                print(n.data,end=" ")
                n=n.nref
            print()
    def backward_traverse(self):
        if self.head==None:
            print("Linked list is empty")
        else:
            print("<<<<<<<<<<<<<<<< Backward Traversing ")
            n=self.head
            while n.nref is not None:
                n=n.nref

            while n is not None:
                print(n.data,end=" ")
                n=n.pref
    def add_node_after(self,data,input):
        new_node=Node(data)
        if self.head==None:
            print("Linked list is empty")
        elif self.head.data==input:
            new_node.nref=self.head.nref
            new_node.pref=self.head
            self.head.nref.pref=new_node
            self.head.nref=new_node

        else:
            n=self.head
            result=True
            while n is not None:
                if input==n.data:
                    new_node.nref =n.nref
                    new_node.pref=n.nref.pref
                    n.nref.pref=new_node
                    n.nref=new_node
                    result=False
                n=n.nref
            if result:
                print(input," Node is not present in the linked list")
    def add_node_before(self,data,input):
        new_node=Node(data)
        if self.head==None:
            print("Linked list is empty")
        elif self.head.data==input:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
        else:
            n=self.head
            result=True
            while n is not None:
                if input==n.data:
                    new_node.nref=n.pref.nref
                    new_node.pref = n.pref
                    n.pref.nref=new_node
                    n.pref=new_node
                    result=False
                n=n.nref
            if result:
                print(input," Node is not present in the Linked list")
    def delete_first(self):
        if self.head==None:
            print("Linked list is empty")
        elif self.head.nref==None:
            self.head=None
        else:
            self.head.nref.pref=None
            self.head=self.head.nref
    def delete_end(self):
        if self.head==None:
            print("Linked list is empty")
        elif self.head.nref==None:
            self.head=None
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
    def delete_inbetween(self,input):
        if self.head==None:
            print("Linked list is empty")
        elif self.head.data==input and self.head.nref==None:
            self.head=None
        elif self.head.data==input:
            self.head.nref.pref=None
            self.head=self.head.nref

        else:
            n= self.head
            result=True
            while n.nref is not None:
                if n.data==input:
                    n.nref.pref=n.pref
                    n.pref.nref=n.nref
                    result=False
                n=n.nref
            if result and n.data is not input:
                print(input," Node not present")
            elif n.data==input:
                n.pref.nref=None
                n.pref=None

l1=Linked_list()
l1.add_front("kalluri")
l1.add_end("reddy")
l1.add_node_before("kumar","reddy")
l1.add_node_after("siva","kalluri")
l1.add_node_after("king","siva")
l1.add_front("delete front")
l1.add_end("delete end")
l1.delete_first()
l1.delete_end()
l1.delete_inbetween("king")
l1.forward_traverse()
l1.backward_traverse()


