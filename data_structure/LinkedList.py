class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    

class LinkedList:
    def __init__(self):
        self.head=None

    def frontIn(self,data):
        node = Node(data,self.head)
        self.head=node

    def backIn(self,data):
        if self.head is None:
            self.head=Node(data)
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next=Node(data)

    def frontOut(self):
        data = self.head.data
        self.head=self.head.next
        return data
    
    def backOut(self):
        if self.head is None:
            return None
        
        itr = self.head
        while itr.next.next:
            itr = itr.next

        data=itr.next.data
        itr.next=None 
        return data
        
    def __str__(self):
        if self.head is None:
            return "Linked List is empty"
        
        result = ""
        itr = self.head
        while itr:
            result += str(itr.data) + " -> "
            itr = itr.next
        return result
        
        
    

llist=LinkedList()
llist.frontIn(5)
llist.frontIn(4)
llist.frontIn(3)
llist.frontIn(2)
llist.frontIn(1)
llist.backIn(6)

data = llist.frontOut()
data2 = llist.backOut()
data3 = llist.backOut()

print(data2,data3, llist)
