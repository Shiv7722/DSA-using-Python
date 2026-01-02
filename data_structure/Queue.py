class Queue:
    def __init__(self):
        self.queue=[]

    def push(self,element):
        self.queue.append(element)

    def pop(self):
        v=None
        if not self.isEmpty():
            v=self.queue[0]
            self.queue=self.queue[1:]
        return v
    
    def isEmpty(self):
        if (self.queue)==0:
            return True
        else:
            return False
    

    def __str__(self):
        return str(self.queue)
    

a = Queue()
print(a.isEmpty())
a.push(3)
a.push(4)
a.push(5)

print(a.isEmpty())
print(a)

x=a.pop()
print("Removed element",x)

