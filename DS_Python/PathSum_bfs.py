#DFS implementation for minDepth

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def newNode(val):
    return Node(val)

def PathSum(root,sum):
    if not root:
        return False
    
    queue = [(root,root.val)]
    while queue:
        nxt_level = []
        for node in queue:
            if sum == node[1] and node[0].left == None and node[0].right == None:
                return True
            if node[0].left:
                nxt_level.append((node[0].left,node[1]+node[0].left.val))
            if node[0].right:
                nxt_level.append((node[0].right,node[1]+node[0].right.val))
        queue = nxt_level
    return False

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
sum = 1
print(PathSum(root,sum))

"""
        1
       / \
      2   3
     / \
    4   5
"""