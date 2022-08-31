from collections import deque


class Node:
  def __init__(self,data):
    self.data = data
    self.right = None
    self.left = None
  
  def insert(self,data):
    root=self
    if root:
      if data<root.data:
        #left
        if root.left:
          root.left.insert(data)
        else:
          root.left = Node(data)
      elif data>root.data:
        #right
        if root.right:
          root.right.insert(data)
        else:
          root.right = Node(data)

  
  def PrintTree(self):
    if self.left:
        self.left.PrintTree()
    print( self.data),
    if self.right:
        self.right.PrintTree()





#-------------NextRight---------------
def NextRight(root,key):
  qu = deque([])
  qu.append(root)
  while len(qu)!=0:
    flag=0
    for i in range(len(qu)):
      node = qu.popleft()
      if flag==1:
        return node.data
      if node.data==key:
        flag=1
      if node.left:
        qu.append(node.left)
      if node.right:
        qu.append(node.right)
    if flag==1:
      return -1










#          4
#    1         5
#      2          6
#  1.5    3          7
#       2.5              



root = Node(4)
root.insert(1)
root.insert(2)
root.insert(1.5)
root.insert(3)
root.insert(5)
root.insert(6)
root.insert(7)
root.insert(2.5)

key = 2
print(NextRight(root,key))