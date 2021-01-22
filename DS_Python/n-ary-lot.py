#BFS 

class Node:
    def __init__(self,val):
        self.val = val
        self.child = []
        
def newNode(val):
    return Node(val)
    
def levelOrderTraversal(root):
    if not root:
        return []
    queue = [root]
    levels = []
    while queue:
        curr_level,next_level = [],[]
        for node in queue:
            curr_level.append(node.val)
            if node.child:
                next_level += node.child
        levels.append(curr_level)
        queue = next_level
    return levels
root = newNode(1)
(root.child).append(newNode(2))
(root.child).append(newNode(3))
(root.child).append(newNode(4))
(root.child[0].child).append(newNode(5))
(root.child[0].child).append(newNode(6))
(root.child[0].child).append(newNode(7))

print(levelOrderTraversal(root))

# TREE

#             1
#          /  / \
#         2   3  4
#       / / \
#      5  6  7

