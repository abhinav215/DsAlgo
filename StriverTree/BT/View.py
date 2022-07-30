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



#-------------LeftVeiw---------------
def leftView(root):
  qu = deque([])
  qu.append([root,0])
  count =0
  ans=[]
  while len(qu)!=0:
    # print(qu)
    front = qu.popleft()
    if count == front[1]:
      ans.append(front[0].data)
      count+=1
    if front[0].left:
      qu.append([front[0].left,count])
    if front[0].right:
      qu.append([front[0].right,count])
  print(ans)


#-------------RightVeiw---------------
def rightSideView( root):
  if root == None:
    return []
  qu = deque([])
  qu.append([root,0])
  ans=[]
  count = 0
  while len(qu) != 0:
    front = qu.popleft()
    number = front[1]
    if number == count:
      ans.append(front[0].data)
      count+=1
    if front[0].right:
      qu.append([front[0].right,number+1])
    if front[0].left:
      qu.append([front[0].left,number+1])
  print(ans)
  return ans


# -------------TopVeiw---------------
def topView(root):
  qu = deque([])
  qu.append([root,0])
  dic ={}
  while len(qu) != 0:
    front = qu.popleft()
    if front[1] not in dic:
      dic[front[1]] = front[0].data 
    if front[0].right:
      qu.append([front[0].right,front[1]+1])
    if front[0].left:
      qu.append([front[0].left,front[1]-1])
  ans=[]
  for i in sorted(dic):
    ans.append(dic[i])
  print(ans)
  return ans


#-------------BottomVeiw---------------
def bottomVeiw(root):
  qu = deque([])
  qu.append([root,0])
  dic={}
  count = 0
  while len(qu) != 0:
    front = qu.popleft()
    dic[front[1]] = front[0].data
    if front[0].right:
      qu.append([front[0].right,front[1]+1])
    if front[0].left:
      qu.append([front[0].left,front[1]-1])
  # print(dic)
  ans=[]
  for key in sorted(dic):
    ans.append(dic[key])
  print(ans)



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
# root.PrintTree()

leftView(root)
rightSideView(root)
topView(root)
bottomVeiw(root)