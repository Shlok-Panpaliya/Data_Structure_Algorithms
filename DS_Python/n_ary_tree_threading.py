class Node:
    def __init__(self,val):
        self.locked = False
        self.parent = None
        self.val = val
        self.child = []
        self.locked_descendants_count = 0
        
def newNode(val):
    return Node(val)

def isLock(node):
    if node.locked == True:
        return True
    else:
        return False
def lock(node):
    #check if any ancestor is locked(O(h)) h == height of node
    def ancestor(root):
        while root:
            if isLock(root) == True:
                return False
            
            root = root.parent
        return True

    def check_descendants(root):
        if root.locked_descendants_count > 0:
            return False
        else:
            return True
    
    if check_descendants(node) and ancestor(node) :
        node.locked = True
        root = node.parent
        
        while(root):
            root.locked_descendants_count += 1
            root = root.parent
        return True
    else:
        return False
    
def unlock(node):

    if node.locked == True:
        node.locked = False
        root = node.parent

        while(root):
            root.locked_descendants_count -= 1
            root = root.parent
        return True
    else:
        return False
    

root = newNode(1)
(root.child).append(newNode(2))
(root.child).append(newNode(3))
(root.child).append(newNode(4))
(root.child[0]).parent = root
(root.child[1]).parent = root
(root.child[2]).parent = root
(root.child[0].child).append(newNode(5))
(root.child[0].child).append(newNode(6))
(root.child[0].child).append(newNode(7))
(root.child[0].child[0]).parent = root.child[0]
(root.child[0].child[1]).parent = root.child[0]
(root.child[0].child[2]).parent = root.child[0]
root.locked = True
print(lock(root.child[0]))
# TREE

#             1
#          /  / \
#         2   3  4
#       / / \
#      5  6  7

