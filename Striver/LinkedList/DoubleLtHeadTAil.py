class Node:
  def __init__(self,data=None,next = None,pre = None):
    self.data = data
    self.next = next
    self.pre = pre

  
class DoubleLinkList:
  def __init__(self):
    self.head= Node("Head",None,None)
    self.tail= Node("Tail",None,self.head)
    self.head.next = self.tail
  
  def insert(self,data):
    start = self.head
    nex = self.head.next
    adding = Node(data,nex,start)
    start.next = adding
    nex.pre = adding
  

  def printingNext(self):
    tvr = self.head.next
    ans = ""
    while tvr:
      ans += str(tvr.data) + "->"
      tvr = tvr.next
    print(ans)


  def printAllRandom(self):
    tvr = self.head.next
    ans = ""
    i=0
    while i<5:
      ans += str(tvr.data) + "->"
      tvr = tvr.next
      i+=1
    print(ans)
    while tvr:
      ans += str(tvr.data)+"<-"
      tvr=tvr.pre
    print(ans)

lt= DoubleLinkList()
lt.insert(1)
lt.insert(2)
lt.insert(3)
lt.insert(4)
lt.insert(5)
lt.insert(6)
lt.printingNext()
lt.printAllRandom()
print(lt.tail.pre.data)
