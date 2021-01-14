
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
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
            self.last = self.last.next
            self.last.next = self.head
    def traverse(self):
        current = self.head
        while(current.next != self.head):
            print(current.data)
            current = current.next
        print(current.data)
        print(current.next.data)
l2 = linkedlist()
l2.append(2)
l2.append(5)
l2.append(1)
l2.append(6)
l2.traverse()
