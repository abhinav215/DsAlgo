

class Node:
  def __init__(self,data):
    self.right = None
    self.left = None
    self.data = data


def maxHeight(root):
  if root == None:
    return 0
  else:
    lH = maxHeight(root.left)
    rH = maxHeight(root.right)
    ans =  1+max(lH,rH)
    return ans


def CheckBinaryTree(root):
  if root == None:
    return 0
  else:
    lH = maxHeight(root.left)
    rH = maxHeight(root.right)
    if lH==-1 or rH == -1:
      return -1
    if (abs(lH-rH)>1):
      return -1
    ans =  1+max(lH,rH)
    return ans



def height(node):
  if node is None:
    return 0
  return 1 + max(height(node.left), height(node.right))

def diameter(root):
  if root is None:
    return 0
  lheight = height(root.left)
  rheight = height(root.right)
  ldiameter = diameter(root.left)
  rdiameter = diameter(root.right)
  return max(lheight + rheight + 1, max(ldiameter, rdiameter))
  





root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(7)
root.right.left.left = Node(5)
root.right.left.left.left = Node(6)
# print(maxHeight(root))
# print(CheckBinaryTree(root))
print(diameter(root))
# print(Solution().Diameter(root))