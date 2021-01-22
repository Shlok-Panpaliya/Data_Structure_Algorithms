#DFS implementation for isBalanced

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def newNode(val):
    return Node(val)

def isBalanced(root,bal):
    if not root:
        return 0,bal
    
    dl,bal = isBalanced(root.left,bal)
    dr,bal = isBalanced(root.right,bal)

    if abs(dl-dr) > 1:
        return 1,False

    return max(dl,dr) + 1,bal

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
x,y = (isBalanced(root,True))
print(y)
"""
        1
       / \
      2   3
     / \
    4   5
"""