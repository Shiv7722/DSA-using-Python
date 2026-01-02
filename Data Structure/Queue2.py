class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue2:
    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self,data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.head is None:
            raise IndexError("Dequeue from an empty queue")
        data = self.head.data
        self.head=self.head.next
        if self.head is None:
            self.tail=None
        return data
    
    def __str__(self):
        if self.head is None:
            return "Queue is empty"

        itr=self.head
        listltr=''
        while itr:
            listltr+=str(itr.data) + ' -> '
            itr=itr.next
        return listltr
    
    def includes(self,data):
        result=False

        if self.head is None:
            return result
        
        itr=self.head
        while itr:
            if itr.data==data:
                result=True
                break
            itr=itr.next
        return result
    



            
        
