#BFS implementation for Max_Depth

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def newNode(val):
    return Node(val)

def height(root):
    queue = [root]
    depth = 0
    while queue:
        nxt_level = [] 
        depth += 1
        for node in queue:
            if node.left:
                nxt_level.append(node.left)
            if node.right:
                nxt_level.append(node.right)
        queue = nxt_level
    return depth


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