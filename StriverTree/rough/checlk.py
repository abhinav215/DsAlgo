


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







def flatten(root):
 
    # Base condition- return if root is None
    # or if it is a leaf node
    if (root == None or root.left == None and
                        root.right == None):
        return
     
    # If root.left exists then we have
    # to make it root.right
    if (root.left != None):
 
        # Move left recursively
        flatten(root.left)
    
        # Store the node root.right
        tmpRight = root.right
        root.right = root.left
        root.left = None
 
        # Find the position to insert
        # the stored value  
        t = root.right
        while (t.right != None):
            t = t.right
 
        # Insert the stored value
        t.right = tmpRight
 
    # Now call the same function
    # for root.right
    flatten(root.right)









root = Node(4)
root.insert(1)
root.insert(2)
root.insert(1.5)
root.insert(3)
root.insert(5)
root.insert(6)
root.insert(7)
root.insert(6.5)
root.insert(3.5)




print(preorder(root))
flatten(root)
while root.right:
  print(root.data)
  root = root.right