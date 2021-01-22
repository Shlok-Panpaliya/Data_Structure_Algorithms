#DFS implementation for minDepth

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def newNode(val):
    return Node(val)

def PathSum(root,sum):

    if root == None:
        return False
    if root.left == None and root.right == None:
        return sum == root.val

    return PathSum(root.left,sum-root.val) or PathSum(root.right,sum-root.val)
    
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
sum = 4
print(PathSum(root,sum))

"""
        1
       / \
      2   3
     / \
    4   5
"""