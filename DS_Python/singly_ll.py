class node:    
    def __init__(self,data):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
        self.last = None
        
    def append(self,data):
        if self.last == None:
            self.head = node(data)
            self.last = self.head
        else:
            self.last.next = node(data)
            self.last = self.last.next
    def traverse(self):
        current = self.head
        while(current != None):
            print(current.data)
            current = current.next
    
    def delete(self,data):
        #if node to be deleted is head node
        if self.head.data == data:
           # current = self.head
            self.head = self.head.next
        #if node to be deleted is last node
        elif self.last.data == data:
            current = self.head
            while(current.next.next):
                current = current.next
            current.next = None
            self.last = current
        #node to be deleted is in between
        else:
            current = self.head.next
            previous = self.head
            while(current.data != data):
                current = current.next
                previous = previous.next
            previous.next = current.next
            current.next = None
            
            
l = linked_list()
l.append(4)
l.append(2)
l.append(1)
l.append(3)
l.traverse()
l.delete(2)
print("after deletion")
l.traverse()