
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.top = None
        self.first = None
    def push(self,data):
        new = node(data)
        if self.top == None:
            self.top = new
            self.first = self.top
        else:
            current = self.top
            while(current.next):
                current = current.next
            current.next = new
            self.top = new
    def pop(self):
        if self.first.next == None:
            self.first = None
        else:
            current = self.first
            while(current.next.next):
                current = current.next
            current.next = None
    def display(self):
        current = self.first
        while(current):
            print(current.data)
            current = current.next
s = stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.display()