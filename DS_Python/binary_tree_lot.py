#BFS implementation for Level Order Traversal

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def newNode(val):
    return Node(val)

def lot(root):
    
    if not root:
        return 
    
    queue = [root]
    ans = []
    while(queue):
        level = []
        for i in range(len(queue)):
            temp = queue.pop(0)
            level.append(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        ans.append(level)
    return ans



root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(5)
print(lot(root))

