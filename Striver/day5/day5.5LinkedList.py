class ListNode:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next

  def reverse(self):
    head = self
    dummy = ListNode()
    while head:
      nex = head.next
      if dummy.val == None:
        dummy.val = head.val
      else:
        head.next = dummy
        dummy = head
      head = nex
    return dummy


  def insertAtBegining(self,data):
    tvr=self
    if tvr.val == None:
      tvr.val = data
      return tvr
    self = ListNode(data,self)
    return self

  def insertAtEnd(self,data):
    pass

  def sizing(self):
    pass

  def middle(self):
    slow = self
    fast = self
    while fast:
      if fast.next==None:
        break
      slow=slow.next
      fast = fast.next.next
    print(slow.val)
    return slow

  def printing(self):
    tvr=self
    a=""
    while tvr:
      a+= str(tvr.val) + "->"
      tvr = tvr.next
    print(a)

def sorting(ll,ll2):
  if ll.val>ll2.val:
    ll,ll2 = ll2,ll
  result = ll
  i = 0
  temp = ll
  while True:
    temp=None
    while ll.val<ll2.val:
      temp = ll
      ll = ll.next
      if ll.next == None:
        ll.next=ll2
        return result
    temp.next = ll2
    ll,ll2 = ll2,ll
    i+=1
    print(i,ll.val,ll2.val,temp.val)


ll= ListNode()
ll = ll.insertAtBegining(10)
ll = ll.insertAtBegining(9)
ll = ll.insertAtBegining(4)
ll = ll.insertAtBegining(3)
ll = ll.insertAtBegining(1)
ll.printing()

# ll.middle()

# rev = ll.reverse()
# rev.printing()



ll2= ListNode()
ll2 = ll2.insertAtBegining(110)
ll2 = ll2.insertAtBegining(19)
ll2 = ll2.insertAtBegining(5)
ll2 = ll2.insertAtBegining(2)
ll2.printing()

sor = sorting(ll2,ll)
sor.printing()