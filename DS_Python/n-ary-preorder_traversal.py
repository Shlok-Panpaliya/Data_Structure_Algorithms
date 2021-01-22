class Node:
    def __init__(self,val):
        self.val = val
        self.child = []

def newNode(key):
    return Node(key)

def preorder(root):
    def dfs(root,ans):
        if not root:
            return 
        ans.append(root.val)
        for child in root.child:
            dfs(child,ans)
        
    
    ans = []
    dfs(root,ans)
    return ans



root = newNode(1)
(root.child).append(newNode(2))
(root.child).append(newNode(3))
(root.child).append(newNode(4))
(root.child[0].child).append(newNode(5))
(root.child[0].child).append(newNode(6))
(root.child[0].child).append(newNode(7))

print(preorder(root))

# TREE

#             1
#          /  / \
#         2   3  4
#       / / \
#      5  6  7

