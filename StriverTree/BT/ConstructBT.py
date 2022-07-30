from collections import deque


class Node:
  def __init__(self,data):
    self.data = data
    self.right = None
    self.left = None


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

#Constructing BT using Preorder and Inorder
def constructBt(inorder,instart,inend,preorder,prestart,preend,hashmap):
  # print("__________________________________________")
  # print(prestart,preend,instart,inend)
  root = None
  if prestart<preend and prestart<preend:
    # print(preorder[prestart])
    root = Node(preorder[prestart])
    index = hashmap[preorder[prestart]]
    # print("left",inorder[instart:index],preorder[prestart+1:index+prestart-instart+1])
    # print("right",inorder[index+1-instart:inend],preorder[prestart+index-instart+1:preend])
    root.left = constructBt(inorder,instart,index,
                              preorder,prestart+1,index+prestart-instart+1,hashmap)
    root.right = constructBt(inorder,index+1,inend,
                              preorder,prestart+index-instart+1,preend,hashmap)
  return root

def answer(inorder,preorder):
  #hashing the preorder root -> inorder-index
  hashmap = {}
  for i in range(len(inorder)):
    hashmap[inorder[i]] = i
  # print(hashmap)
  root = constructBt(inorder,0,len(inorder),preorder,0,len(preorder),hashmap)
  print(levelorder(root))

inorder =[40,20,50,10,60,30]
preorder=[10,20,40,50,30,60]
answer(inorder,preorder)


##################################################################
###################################################################
##################################################################
###################################################################
##################################################################
###################################################################
##################################################################
###################################################################





#Constructing BT using PostOrder and Inorder

def ConstructBtWithInANDPre(inorder,instart,inend,postorder,postart,poend,dic):
  # print(inorder[instart:inend],postorder[postart:poend],postart,poend)
  root=None
  if postart<poend and instart<inend:
    root = Node(postorder[poend-1])
    pointer = dic[postorder[poend-1]]
    root.left = ConstructBtWithInANDPre(inorder,instart,pointer,postorder,postart,postart+pointer-instart,dic)
    root.right = ConstructBtWithInANDPre(inorder,pointer+1,inend,postorder,postart+pointer-instart,poend-1,dic)
  return root

def answer(inorder,postorder):
  dic = {}
  for i in range(len(inorder)):
    dic[inorder[i]] =i
  root =ConstructBtWithInANDPre(inorder,0,len(inorder),postorder,0,len(postorder),dic)
  print(levelorder(root))


inorder =[40,20,50,10,60,30]
postorder = [40,50,20,60,30,10]
answer(inorder,postorder)