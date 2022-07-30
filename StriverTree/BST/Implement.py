import sys


class Node:
  def __init__(self,data):
    self.right = None
    self.left = None
    self.data = data

def inorder(root):
  ans =[]
  if root:
    ans = inorder(root.left)
    ans.append(root.data)
    ans+= inorder(root.right)
  return ans

# ---------------Insertion---------------------
#- -------------TC = log(n)----------------
def insert(root,data):
    if root.data:
      if data < root.data:
        if root.left == None:
          root.left = Node(data)
        else:
          insert(root.left,data)
      elif data>root.data:
        if root.right==None:
          root.right = Node(data)
        else:
          insert(root.right,data)
    else:
      root.data = data


# ---------------Deletion---------------------
#- -------------TC = log(n)----------------
def searchBTindelete(root,target,parent):
  # print(root.data)
  if root==None:
    return None
  if root.data==target:
    return root
  if root.data>target:
    parent[0] = root
    return searchBTindelete(root.left,target,parent)
  if root.data<target:
    parent[0] = root
    return searchBTindelete(root.right,target,parent)

def delete(root,key):
  parent=[-1]
  target = searchBTindelete(root,key,parent)
  if parent[0] ==-1:
    rightside= target.right
    leftside = target.left
    root = leftside
    tvr = leftside
    while tvr.right!=None:
      tvr = tvr.right
    tvr.right = rightside
    return root
  print(parent[0].data)
  rightside= target.right
  leftside = target.left
  if parent[0].data>key:
    parent[0].left = leftside
  if parent[0].data<key:
    parent[0].right = leftside
  tvr = leftside
  while tvr.right!=None:
    tvr = tvr.right
  tvr.right = rightside
  return root


# ---------------Search---------------------
#- -------------TC = log(n)----------------
def searchBT(root,target):
  print(root.data)
  if root==None:
    return None
  if root.data==target:
    return root
  if root.data>target:
    return searchBT(root.left,target)
  if root.data<target:
    return searchBT(root.right,target)


# ---------------Ceil---------------------
#- -------------TC = log(n)----------------
def ceiling(root,key,ceill):
  if root==None:
    return ceill[0]
  print(root.data)
  if key == root.data:
    return key
  if key<root.data:
    ceill[0]=root.data
    return ceiling(root.left,key,ceill)
  if key>root.data:
    return ceiling(root.right,key,ceill)
  

# ---------------Floor---------------------
#- -------------TC = log(n)----------------
def flooring(root,key,ans):
  if root==None:
    return ans[0]
  print(root.data,ans[0])
  if root==key:
    return ans[0]
  if key<root.data:
    return flooring(root.left,key,ans)
  ans[0]=root.data
  return flooring(root.right,key,ans)


#----------Kth smallest ELe----------------
def KthSmallest(k,count,root):
  if root:
    KthSmallest(k,count,root.left)
    count[0] += 1
    if count[0] == k:
      print(root.data)
      return root.data
    KthSmallest(k,count,root.right)


def CheckValidBST( root,maxlimit,minlimit):
  if root:
    if root.data>maxlimit or root.data<minlimit:
      return False
    return CheckValidBST(root.left,root.data,minlimit) and CheckValidBST(root.right,maxlimit,root.data)
  return True


def lca(root,a,b):
  if root:
    if root.data>a and root.data>b:
      return lca(root.left,a,b)
    if root.data<a and root.data<b:
      return lca(root.right,a,b)
    return root.data


def construct(preorder,index,n,ub):
  if preorder[index[0]]<ub[0]:
    root = Node(preorder[index[0]])
    index[0] += 1
    if index[0]==n:
      return root
    root.left = construct(preorder,index,n,[root.data])
    if index[0]==n:
      return root
    root.right = construct(preorder,index,n,ub)
    return root
  return None


def Precessor(root,p,val):
  if root:
    print(root.data,val,p)
    if root.data == val:
      tvr = root
      if root.right:
        p[0] = root.right
        while root.left:
          root=root.left
        p[0]=root.data
        print(p,"j")
    elif root.data>=val:
      p[0]=root.data
      Precessor(root.left,p,val)
    else:
      Precessor(root.right,p,val)







root = Node(4)
insert(root,1)
insert(root,0.5)
insert(root,0.2)
insert(root,0.7)
insert(root,2)
insert(root,1.5)
insert(root,3)
insert(root,5)
insert(root,6)
insert(root,7)
insert(root,6.5)
insert(root,3.5)



#                4
#          1            5
#     0.5       2          6
#   0.2 0.7  1.5   3          7
#                    3.5   6.5
#              


# target = 6.5
# print(searchBT(root,target))


# ans = [-1]
# key = 6.4
# print(ceiling(root,key,ans))



# ans = [-1]
# key = 6.4
# print(flooring(root,key,ans))


# root = delete(root,4)

# key = 3
# count = [0]
# KthSmallest(key,count,root)



# print(CheckValidBST(root,sys.maxsize,-sys.maxsize))

# a=3.5
# b = 0.7
# print(lca(root,a,b))


# index=[0]
# preorder = [8,5,1,7,10,12]
# n = len(preorder)
# ub = [sys.maxsize]
# root  = construct(preorder,index,n,ub)
# print(inorder(root),"ans")

s = [None]
val =2
Precessor(root,s,val)
print(s)