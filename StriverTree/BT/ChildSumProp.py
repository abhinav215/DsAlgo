

from collections import deque


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

def preorder(root):
  ans = []
  if root:
    ans.append(root.data)
    ans+=preorder(root.left)
    ans+=preorder(root.right)
  return  ans



def childSumProp(root):
  if root:
    child =0
    if root.right:
      child += root.right.data
    if root.left:
      child += root.left.data


    if child >= root.data:
      root.data = child
    else:
      if root.left:
        root.left.data = root.data
      if root.right:
        root.right.data = root.data

    childSumProp(root.left)
    childSumProp(root.right)

    change = 0
    if root.left:
      change+=root.left.data
    if root.right:
      change += root.right.data
    print(root.data,change)
    if root.left or root.right:
      root.data = change
  return 
    


root = Node(40)
root.right = Node(20)
root.left = Node(10)
root.right.right = Node(40)
root.left.right = Node(3)
root.right.left = Node(30)
root.left.left = Node(2)


#          40
#    10         20
#  2    3     30    40  



print(preorder(root))
print(root.data)
childSumProp(root)
print(preorder(root))