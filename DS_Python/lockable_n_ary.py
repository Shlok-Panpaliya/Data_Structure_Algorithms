class Node:
    def __init__(self,val):
        self.locked = False
        self.parent = None
        self.val = val
        self.child = []
        

def newNode(val):
    return Node(val)

def isLock(node): #O(1)
    if node.locked == True:
        return True
    else:
        return False
def lock(node): #(O(N+H))

    #check if any ancestor is locked(O(h)) h == height of node
    def ancestor(root):
        
        while root.parent:
            if isLock(root) == True:
                return False
            
            root = root.parent
        return True

    #check if any decendent is locked
    #Do a level order traversal(O(N)) N = number of descendents
    def desendents(root):

        queue = [root]
        while queue:
            level = []
            next_level = []
            for node in queue:
                if isLock(node) == True:
                    return False
                
            #  level.append(node.val)
                if node.child:
                    next_level += node.child
                
            queue = next_level 
            #ans.append(level)
        return True
    return ancestor(node) and desendents(node)

    
def unlock(node):

    if node.locked == True:
        node.locked = False
    



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
root.child[0].locked = True
print(lock(root.child[1]))
# TREE

#             1
#          /  / \
#         2   3  4
#       / / \
#      5  6  7

