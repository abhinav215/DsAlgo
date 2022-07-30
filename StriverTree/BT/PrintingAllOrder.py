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




# ------INORDER---------------
def inorder(root):
  ans =[]
  if root:
    ans = inorder(root.left)
    ans.append(root.data)
    ans+= inorder(root.right)
  return ans



# ------PREORDER---------------
def preorder(root):
  ans = []
  if root:
    ans.append(root.data)
    ans+=preorder(root.left)
    ans+=preorder(root.right)
  return  ans



# ------POSTORDER---------------
def postorder(root):
  ans = []
  if root:
    ans+=preorder(root.left)
    ans+=preorder(root.right)
    ans.append(root.data)
  return  ans



# ------LEVELORDER---------------
def levelorder(root):
  qu = deque([])
  qu.append(root)
  ans = []
  while len(qu)!=0:
    front = qu.popleft()
    ans.append(front.data)
    if front.left:
      qu.append(front.left)
    if front.right:
      qu.append(front.right)
  # print(ans)
  return ans



# ------ZIG-ZAG-ORDER---------------
def zigZagTrivarsal(root):
  qu = deque([])
  qu.append(root)
  ans=[]
  leftToRight=True
  while len(qu) !=0:
    iteration = []
    for i in range(len(qu)):
      front = qu.popleft()
      iteration.append(front.data) 
      if front.left:
        qu.append(front.left)
      if front.right:
        qu.append(front.right)
    if leftToRight:
      pass
    else:
      iteration.reverse()
    ans+= iteration
    leftToRight = not leftToRight
  # print(ans)
  return ans



#---------BOUNDARY-ORDER ------------
def inorderedge(root,res):
  ans =[]
  if root:
    ans = inorderedge(root.left,res)
    ans.append(root.data)
    ans += inorderedge(root.right,res)
    if root.left==None and root.right==None:
      res.append(root.data)
  return ans

def boundaryTrivarsal(root):
  ans = [root.data]

    #left
  if root.left:
    tvr = root.left
    leftSide =[]
    while True:
      if tvr.left:
        val = tvr.data
        tvr = tvr.left
      elif tvr.right:
        val = tvr.data
        tvr = tvr.right
      else:
        break
      leftSide.append(val)
    # print(leftSide)

    #Edge
  res =[]
  inorderedge(root,res)
  # print(res,"res")
  
    #right
  if root.right:
    tvr = root.right
    rightSide =[]
    while True:
      if tvr.right:
        val = tvr.data
        tvr = tvr.right
      elif tvr.left:
        val = tvr.data
        tvr = tvr.left
      else:
        break
      rightSide.append(val)
      # ans.append(val)
    rightSide.reverse()
    # print(rightSide)
  ans = ans+leftSide+res+rightSide
  return ans



# ----------VERTICAL-ORDER(using levelorder)------------
def verticalOrder(root):
  qu = deque([])
  qu.append([root,0])
  dic={}
  while len(qu) != 0:
    front = qu.popleft()
    if front[1] not in dic:
      dic[front[1]] = [front[0].data]
    else:
      dic[front[1]].append(front[0].data)
    if front[0].right:
      qu.append([front[0].right,front[1]+1])
    if front[0].left:
      qu.append([front[0].left,front[1]-1])
  # print(dic)
  ans=[]
  print(dic)
  ans=[]
  for key in sorted(dic):
    dic[key].sort()
    ans.append(dic[key])
  return ans

#ANOTHER VERTICAL(USING MAP)
def preorder(root,x,m):
  if root:
    if x in m:
      m[x].append(root.val)
    else:
      m[x] = [root.val]
    preorder(root.left,x-1,m)
    preorder(root.right,x+1,m)
            
def verticalTraversal( root):
  m ={}
  preorder(root,0,m)
  print(m)
  ans=[]
  for key in sorted(m):
    m[key].sort()
    ans.append(m[key])
  return ans










#          4
#    1         5
#      2          6
#  1.5   3          7



root = Node(4)
root.insert(1)
root.insert(2)
root.insert(1.5)
root.insert(3)
root.insert(5)
root.insert(6)
root.insert(7)
# root.PrintTree()


# print(inorder(root))
# print(preorder(root))
# print(postorder(root))
# print(levelorder(root))
# print(zigZagTrivarsal(root))
# print(boundaryTrivarsal(root))
print(verticalOrder(root))

