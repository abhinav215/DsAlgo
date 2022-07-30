#          4
#    1         5
#      2          6
#        3          7






class Queue(object):
  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    if not self.is_empty():
      return self.items.pop()

  def is_empty(self):
    return len(self.items) == 0

  def peek(self):
    if not self.is_empty():
      return self.items[-1].value

  def __len__(self):
    return self.size()

  def size(self):
    return len(self.items)

class Node:
  def __init__(self,data):
    self.right = None
    self.left = None
    self.data = data

  def insert(self,data):
    if self.data:
      if data < self.data:
        if self.left == None:
          self.left = Node(data)
        else:
          self.left.insert(data)
      elif data>self.data:
        if self.right==None:
          self.right = Node(data)
        else:
          self.right.insert(data)
    else:
      self.data = data

  def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
  
#quere
  # Level by level traversal
  def levelTransverse(self,root):
    print(root)
    if root is None:
      return
    q = []
    q.append(root)
    res = ""
    while len(q)>0:
      print("emergenct")
      res += str(q[0].data)+"-" 
      node = q.pop(0)
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    return res

  # Inorder traversal
  #left->root->right
  def inorderTransverse(self,root):
    res = []
    if root:
      res = self.inorderTransverse(root.left)
      res.append(root.data)
      res = res + self.inorderTransverse(root.right)
    return res

  # Preorder traversal
  # Root -> Left ->Right
  def preorderTransverse(self,root):
    res = []
    if root:
      res.append(root.data)
      res = res + self.preorderTransverse(root.left)
      res = res + self.preorderTransverse(root.right)
    return res

  # Postorder traversal
  # Left ->Right -> Root
  def postorderTransverse(self,root):
    res = []
    if root:
      res = self.postorderTransverse(root.left)
      res = res + self.postorderTransverse(root.right)
      res.append(root.data)
    return res


  def finder(self,findValue):
    if findValue == self.data:
      print("mill gaya")
    elif findValue>self.data:
      if findValue == self.right.data:
        print("right mai milla")
      else:
        self.right.finder(findValue)
    elif findValue<self.data:
      if findValue == self.left.data:
        print("left mai milla")
      else:
        self.left.finder(findValue)

root = Node(4)
root.insert(1)
root.insert(2)
root.insert(3)
root.insert(5)
root.insert(6)
root.insert(7)

# root.finder(4)
# root.finder(3)
# root.finder(6)
# root.finder(1)
# root.finder(5)
# root.PrintTree()
# print(root.inorderTransverse(root))
# print(root.preorderTransverse(root))
# print(root.postorderTransverse(root))
print(root.levelTransverse(root))
