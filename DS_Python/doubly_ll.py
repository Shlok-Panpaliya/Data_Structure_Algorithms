class node:
    def __init__(self,data):
            self.data = data
            self.next = None
            self.prev = None
class linkedlist:
    def __init__(self):
        self.head = None
        self.last = None
    def append(self,data):
        if self.last is None:
            self.head = node(data)
            self.last = self.head
        else:
            self.last.next = node(data)
            self.last.next.prev = self.last
            self.last = self.last.next
    def traverse(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
    def reversetraverse(self):
        current = self.last
        while(current):
            print(current.data)
            current = current.prev
    def delete(self,data):
        if(self.head.data == data):
            current = self.head
            self.head = current.next
            current.next = None
            current.prev = None
            self.head.prev = None
        elif(self.last.data == data):
            current = self.head
            while(current.next.next):
                current = current.next
            current.next = None
            current.next.prev = None
            self.last = current
        else:
            current = self.head.next
            previous = self.head
            while(current.data != data):
                current = current.next
                previous = previous.next
            previous.next = current.next
            current.next.prev = previous
            current.next = None
            current.prev = None
l1 = linkedlist()
l1.append(1)
l1.append(2)
l1.append(5)
l1.append(3)
l1.append(6)
print('traverse')
l1.traverse()
print('reverse traverse')
l1.reversetraverse()
l1.delete(3)
print('traverse')
l1.traverse()