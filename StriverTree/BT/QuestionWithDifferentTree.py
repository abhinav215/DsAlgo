


class Node:
  def __init__(self,data):
    self.right = None
    self.left = None
    self.data = data


# ========CHECK SYMMETRY OF TREE=======
def symmetrical(left,right):
  if left==None or right==None:
    return left == right
  if left.data != right.data:
    return False
  return symmetrical(left.left,right.right) and symmetrical(left.right,right.left)

def symmetryCheck(root):
  return root==None or symmetrical(root.left,root.right)


# ========IN A COMPLETE TREE FIND NUMBER OF NODE=======
def leftHeight(root):
  count = 0
  while root:
    count+=1
    root = root.left
  return count

def rightHeight(root):
  count = 0
  while root:
    count+=1
    root = root.right
  return count

def CountNodeInCompleteTree(root):
  if root:
    lh = leftHeight(root)
    rh = rightHeight(root)
    if lh==rh:
      print((2<<lh)-1,lh,"eq")
      return (1<<lh)-1
    print(1+CountNodeInCompleteTree(root.left)+CountNodeInCompleteTree(root.right))
    return 1+CountNodeInCompleteTree(root.left)+CountNodeInCompleteTree(root.right)


# root = Node(4)
# root.right = Node(1)
# root.left = Node(1)
# root.right.right = Node(2)
# root.left.left = Node(2)
# root.right.left = Node(3)
# root.left.right = Node(3)
# root.left.right.left = Node(5)
# root.right.left.right = Node(5)
# print(symmetryCheck(root))


#         4
#      1      1
#    2   3  3   2
#       5    5





root = Node(4)
root.right = Node(1)
root.left = Node(1)
root.right.right = Node(2)
root.left.left = Node(2)
root.left.left.left = Node(7)
root.left.left.right = Node(10)
root.right.left = Node(3)
root.left.right = Node(3)
root.left.right.left = Node(5)
root.left.right.right = Node(11)

#                 4
#        1                  1
#    2        3        3         2
#  7   10   5   11 

print(CountNodeInCompleteTree(root))