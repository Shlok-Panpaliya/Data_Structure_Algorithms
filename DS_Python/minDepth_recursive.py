#DFS implementation for minDepth

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def newNode(val):
    return Node(val)

def minDepth(root):
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    elif not root.left:
        return 1+minDepth(root.right)
    elif not root.right:
        return 1+minDepth(root.left)
    else:
        return 1+min(minDepth(root.left),minDepth(root.right))

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
print(minDepth(root))

"""
        1
       / \
      2   3
     / \
    4   5
"""