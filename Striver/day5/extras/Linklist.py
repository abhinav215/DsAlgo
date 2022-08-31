class Node:
  def __init__(self,data=None,next=None) -> None:
    self.data= data
    self.next=next


class LinkList:
  def __init__(self):
    self.head=None

  def insertAtBegining(self,data):
    node= Node(data,self.head)
    self.head = node
  
  
  def insertAtEnd(self,data):
    if self.head==None:
      self.head=Node(data,None)
      return
    itr = self.head
    while itr.next:
      itr=itr.next
    itr.next = Node(data,None)


  def insertAt(self,position,data):
    print(position,self.sizing())
    if position<0 or position>=self.sizing():
      print("Invalid Index")
      return
    if position ==0:
      self.insertAtBegining(data)
      return
    itr = self.head
    count = 0
    while itr:
      if count==position-1:
        break
      count+=1
      itr=itr.next
    itr.next = Node(data,itr.next)


  def sizing(self):
    count=0
    itr = self.head
    while itr:
      count+=1
      itr = itr.next
    # print(count)
    return count


  def removing(self,position):
    if position<0 or position>=self.sizing():
      print("Invalid Index")
      return
    if position==0:
      self.head = self.head.next
      return

    itr = self.head
    count=0
    while itr:
      if count == position-1:
        break
      itr = itr.next
      count+=1 
    itr.next = itr.next.next


  def printing(self):
    if self.head is None:
      print("list is blank")
      return 
    itr= self.head
    ans = ""
    while itr:
      ans += str(itr.data)+"-->"
      itr=itr.next
    print(ans)


ll= LinkList()
ll.insertAtBegining(4)
ll.insertAtBegining(3)
ll.insertAtBegining(2)
ll.insertAtEnd(1)
ll.insertAt(2,10)#(position,value)
# ll.sizing()
# ll.removing(1)
ll.printing()