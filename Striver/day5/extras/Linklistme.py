class Node:
  def __init__(self,data,next) -> None:
      self.data = data
      self.next = next

class LinkList:
  def __init__(self) -> None:
    self.head = None

  def AddBegining(self,data):
    self.head  = Node(data,self.head)

  def printing(self):
    out = ""
    trv = self.head
    while trv:
      out += str(trv.data) + " -> "
      trv = trv.next
    print(out)
  
  def printingreverse(self,ll):
    tvr = ll.head
    while tvr:
      self.AddBegining(tvr.data)
      tvr= tvr.next
      print("emergency")
    return self
    # pass
    



ll = LinkList()
ll.AddBegining(1)
ll.AddBegining(2)
ll.AddBegining(3)
ll.printing()

ll2 = LinkList()
a = ll2.printingreverse(ll)
print(a)