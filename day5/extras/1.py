# Input Format: 
# head = [3,6,8,10]
# This means the given linked list is 3->6->8->10 with head pointer at node 3.

# Result:
# Output = [10,6,8,3]
# This means, after reversal, the list should be 10->6->8->3 with the head pointer at node 10.

class Node:
  def __init__(self,data = None,next = None):
    self.data = data
    self.next = next

class LinkList:
  def __init__(self):
    self.head = None

  def insertAtBegining(self,data):
    self.head = Node(data, self.head)

  def printing(self):
    if self.head is None:
      print("list is blank")
      return
    itr = self.head
    ans = ""
    while itr:
      ans+=str(itr.data)+"-->"
      itr = itr.next
    print(ans)

  def reverse(self):
    if self.head == None:
      print("list is blank")
      return
    if self.head.next == None:
      return
    dummyNode = Node(None,None)
    itr = self.head
    for i in range(5):
    # while self.head!=None:
      nextOne = LinkList()
      nextOne.head = Node(itr.next,None)
      itr.next = dummyNode
      dummyNode = self.head
      itr.data = nextOne
      print(itr.data,itr.next,dummyNode.data,nextOne.head.data )
    return nextOne


    



ll= LinkList()
ll.insertAtBegining(10)
print(ll.head.data)
ll.insertAtBegining(10)
ll.insertAtBegining(10)
ll.insertAtBegining(10)
ll.insertAtBegining(10)
ll.insertAtBegining(8)
ll.insertAtBegining(6)
ll.insertAtBegining(3)
ll.printing()
ll = ll.reverse()
print(ll.head)
# ll.printing()
# print(ll.head.data)