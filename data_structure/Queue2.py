class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue2:
    def __init__(self):
        self.head=None

    def enqueue(self,data):
        node=Node(data, self.head)
        self.head=node

    def dequeue(self):
        data = self.head.data
        self.head=self.head.next
        return data
    
    def __str__(self):
        if self.head is None:
            return "Queue is empty"

        itr=self.head
        listltr=''
        while itr.next:
            listltr+=str(itr.data) + ' -> '
            itr=itr.next
        return listltr
    
    def includes(self,data):
        result=False
        itr=self.head
        while itr.next:
            if itr.data==data:
                result=True
                break
            itr=itr.next
        return result
    

mylist = Queue2()
mylist.enqueue(3)
mylist.enqueue(3)
mylist.enqueue(3)
mylist.enqueue(3)
print(mylist)
            
        
