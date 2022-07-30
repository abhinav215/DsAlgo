def top(st):
  n = len(st)
  return st[n-1]


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

  def PrintTree(self):
    if self.left:
      self.left.PrintTree()
    print( self.data),
    if self.right:
      self.right.PrintTree()

  def IteratePreorder(self,root):
    ans = []
    if root == None:
      return ans
    lt =[]#stack
    lt.append(root)
    while(len(lt)!=0):
      print("emergency")
      root = lt.pop()
      ans.append(root.data)
      if root.right != None:
        lt.append(root.right)
      if root.left != None:
        lt.append(root.left)
    return ans


  def IterateInorder(self,root):
    ans = []
    st=[]
    node = root
    while(True):
      if node!= None:
        st.append(node)
        node = node.left
      else:
        if (len(st)==0):
          break
        node = st.pop()
        ans.append(node.data)
        node = node.right
    return ans


  def IteratePostorder2(self,root):
    #top fuction copy kar laina 
    st = []
    ans = []
    cur = root
    while(cur!=None or len(st)!=0):
      # print("emergency",len(st),cur.data if cur != None else "none",temp.data)
      if cur != None:
        st.append(cur)
        cur = cur.left
      else:
        temp = top(st).right
        if temp == None:
          temp = st.pop()
          ans.append(temp.data)
          while (len(st)!=0 and temp == top(st).right):
            temp = st.pop()
            ans.append(temp.data)
        else:
          cur = temp
    return ans


  def IteratePostorder(self,root):
    ans = []
    st1 = []
    st2=[]
    if root==None:
      return ans
    st1.append(root)
    while(len(st1)!=0):
      print("emergency",len(st1),root.data)
      top = st1.pop()
      root = top
      st2.append(root)
      if (root.left != None):
        st1.append(root.left)
      if (root.right != None):
        st1.append(root.right)
    # print(st2)
    while len(st2)!=0:
      top = st2.pop()
      ans.append(top.data)
    return ans

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.right = Node(4)
root.left.left.right.right = Node(5)
root.left.left.right.right.right = Node(6)
root.right = Node(7)
root.right.left = Node(8)
# root.PrintTree()
# print(root.IteratePreorder(root))
# print(root.IteratePostorder(root))
print(root.IteratePostorder2(root))
# print(root.IterateInorder(root))