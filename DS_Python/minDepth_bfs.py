#BFS implementation for minDepth

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
    level = 0
    queue = [root]
    while queue:
        level += 1
        nxt_level = []
        for node in queue:
            if node.left == None and node.right == None:
                return level
            if node.left:
                nxt_level.append(node.left)
            if node.right:
                nxt_level.append(node.right)
        queue = nxt_level


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