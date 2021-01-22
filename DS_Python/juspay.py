import threading

class Node:
	def __init__(self,val):
        self.parent = None
        self.val = val
        self.child = []
        self.count_locked_succesor = 0
        self._lock = threading.Lock()
        
#make thread safe  
def lock(root):  
 # atomic(root) in java
  with self._lock:
    if root.locked == True: 
      return False
  	root.locked = True  #What is node? #it should be root wrote it wrong
  
  #check for ancestor
  def ancestor(root):
    node = root.parent
    while(node != None):
        if node.locked == True:
          return False
        else:
          node.check_succesor += 1
          node = node.parent
    return True

  #keep a track if any succesor is locked
  #keep a count on number of succesor locked 
  def succesor(root):
    if root.count_locked_succesor > 0:
      return False
    elif root.check_succesor > 0:
      return False
    else:
      node = root.parent
      while(node != None):
        node.count_locked_succesor += 1
        node = node.parent
      return True
	#if both are succesful we will have to update the count of locked succesor for all ancestor of node else return False
  
  if successor(root) == True and ancestor(root) == True:
      return True       
  else:
  	  node.locked = False
      return False

def unlock(node):
  #if already unlocked return False
  #if locked make boolean value False and update count_locked_succesor and return True
  
  if node.locked == True:
  	node.locked = False
    temp = node.parent
    while(temp):
    	temp.count_locked_succesor -= 1
      temp.check_succesor -= 1
      temp = temp.parent
    return True
  else:
  	return False
  	
    
  
def __init__(main):
	#make sample entries for tree
  root = Node(1)
  (root.child).append(Node(2))
  (root.child).append(Node(3))
  (root.child).append(Node(4))
  (root.child[0].child).append(Node(5))
  (root.child[0].child).append(Node(6))
  (root.child[0].child).append(Node(7))
  
 # 			   1
 #           / / \
 #          2  3   4
 #        / / \
 #       5  6 7
  
  print(lock(node))
  print(unlock(node))
  