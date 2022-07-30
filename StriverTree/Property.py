



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

#---------------Max Depth ------------------
def maxDepth(root):
  if root:
    return 1+max(maxDepth(root.right),maxDepth(root.left))
  else:
    return 0

#----------------check if tree is balances----------
def checkBalanced(root):
  if root:
    lH = checkBalanced(root.left)
    rH = checkBalanced(root.right)
    if lH ==-1 or rH==-1:
      return -1
    if lH-rH >= 0 and lH-rH<=1:
      return 1+(lH-rH)
    else:
      return -1
  else:
    return 0


#------------Diameter ------------------------
def diameter(root,maxi):
  if root:
    lH = diameter(root.left,maxi)
    rH = diameter(root.right,maxi)
    maxi[0] = max(maxi[0],lH+rH)
    return 1+max(lH,rH)
  return 0


#----------Max Path---------------
def maxPath(root,maxi):
  if root:
    leftside = maxPath(root.left,maxi)
    rightside = maxPath(root.right,maxi)
    summ = root.data + leftside+rightside
    maxi[0] = max(maxi[0],summ)
    return root.data + max(leftside,rightside)
  return 0

#-----------Root To Node Path--------
def rootToNodePath(root,ans,target):
  if root:
    ans.append(root.data)
    if root.data == target:
      return True
    leftside = rootToNodePath(root.left,ans,target)
    if leftside:
      return True
    rightside = rootToNodePath(root.right,ans,target)
    if rightside:
      return True
    ans.pop()
  return False


#-----------LOWEST-COMMON-ANCESTORS--------
def lowestCommonAncestors(data1,data2,root):
  if root:
    if root.data == data1:
      return data1
    if root.data == data2:
      return data2
    leftside = lowestCommonAncestors(data1,data2,root.left)
    rightside = lowestCommonAncestors(data1,data2,root.right)
    if leftside == None and rightside==None:
      return None
    if leftside != None and rightside!=None:
      return root.data
    if leftside==None:
      return rightside
    return leftside
  return None


#-----------MAX-WIDTH ---------------
def width(root):
  qu = deque([])
  qu.append([root,0])
  width = 0
  while len(qu) != 0:
    mini =100000
    maxi =-1
    mininal = qu[-1][1]
    for i in range(len(qu)):
      root,number = qu.popleft()
      print(number)
      mini = min(mini,number)
      maxi = max(maxi,number)
      if root.left:
        qu.append([root.left,(number<<1)+1-mininal])
      if root.right:
        qu.append([root.right,(number<<1)+2-mininal])
    width= max(width,maxi-mini+1)
  print(width)
  return width


#-----------CHILD-SUM-PROP---------------
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
    if root.left or root.right:
      root.data = change
  return 
    

#----------NODE-AT-DISTANCE-K------------
def nodesAtDistanceK(root,target,k):
  qu = deque([])
  qu.append(root)
  childToParentHashMap = {}
  while len(qu)!=0:
    front = qu.popleft()
    if front.left:
      childToParentHashMap[front.left] = front
      qu.append(front.left)
    if front.right:
      childToParentHashMap[front.right] = front
      qu.append(front.right)
  # print(childToParentHashMap)

  #find targetNode is target.data is give ... we want address ... here directly address is given
  # TargetNode = find(Node)

  qu.append(target)
  distance = 0
  visitedNodeHashMap={}
  while len(qu)!=0:
    for i in range(len(qu)):
      root = qu.popleft()
      visitedNodeHashMap[root] = True
      if root.left and root.left not in visitedNodeHashMap:
        qu.append(root.left)
      if root.right and root.right not in visitedNodeHashMap :
        qu.append(root.right)
      if root in childToParentHashMap and childToParentHashMap[root] not in visitedNodeHashMap:
        qu.append(childToParentHashMap[root])
    distance+=1
    if distance ==k:
      break
  ans =[]
  for ele in qu:
    ans.append(ele.data)
  print(ans)
    
#----------MINIMUM-TIME-TO-BURN-TREE----------
def minTimeToBurn(root,target):
  qu = deque([])
  qu.append(root)
  childToParent = {}
  while len(qu)!=0:
    root = qu.popleft()
    if root.left:
      childToParent[root.left] = root
      qu.append(root.left)
    if root.right:
      childToParent[root.right] = root
      qu.append(root.right)
  #print(childToParent)
  qu.append(target)
  visited={}
  time = -1
  while len(qu)!=0:
    for i in range(len(qu)):
      front = qu.popleft()
      visited[front]=True
      if front.left and front.left not in visited:
        qu.append(front.left)
      if front.right and front.right not in visited:
        qu.append(front.right)
      if front in childToParent and childToParent[front] not in visited:
        qu.append(childToParent[front])
    time+=1
  print(time)



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


#          4
#    1         5
#      2          6
#  1.5   3          7
#          3.5   6.5
#              


# print(maxDepth(root))

# print(checkBalanced(root))

# maxi = [0]
# diameter(root,maxi)
# print(maxi[0])

# maxi = [0]
# maxPath(root,maxi)
# print(maxi[0])

# target = 1.5
# ans=[]
# print(rootToNodePath(root,ans,target))
# print(ans)

# print(lowestCommonAncestors(1.5,3.5,root))

# print(width(root))

# childSumProp(root)
# print(preorder(root))

# target =root.left
# k = 2
# nodesAtDistanceK(root,target,k)


target =root.left
minTimeToBurn(root,target)