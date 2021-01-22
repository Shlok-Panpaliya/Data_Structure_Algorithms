#DFS implementation for Max_Depth

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def newNode(val):
    return Node(val)

def height(root):
    if not root:
        return 0
    
    dl = height(root.left)
    dr = height(root.right)

    return max(dl,dr) + 1

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
print(height(root))

"""
        1
       / \
      2   3
     / \
    4   5
"""