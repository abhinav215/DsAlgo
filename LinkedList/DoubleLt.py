class DoubleLtNode:
  def __init__(self,data=None,next = None,pre = None):
    self.data = data
    self.next = next
    self.pre = pre

  def insert(self,data):
    head = self
    #abhi jo head.next hai uska kuch kar
    tvr = head.next
    head.next = DoubleLtNode(data,head.next,head)
    if tvr:
      tvr.pre = head.next

  def printingNext(self):
    tvr = self.next
    ans = ""
    while tvr:
      ans += str(tvr.data) + "->"
      tvr = tvr.next
    print(ans)
  

  def printAllRandom(self):
    tvr = self.next
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

lt = DoubleLtNode()
lt.insert(1)
lt.insert(2)
lt.insert(3)
lt.insert(4)
lt.insert(5)
lt.insert(6)
lt.printingNext()
lt.printAllRandom()
