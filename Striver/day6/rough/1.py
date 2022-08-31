

class ListNode:
  def __init__(self, x=None,next=None):
    self.val = x
    self.next = next

  def addAtBegining(self,data):
    if self.val ==None:
      self.val = data
      self.next = None
      return self
    return  ListNode(data,self)

  def insertNode(self,node):
    tvr= self
    if self.val==None:
      self = node
      return self
    while tvr.next:
      tvr=tvr.next
      # print("tvr",tvr.val)
    tvr.next = node
    return self

  def skipping(self,n):
    tvr = self
    while n>0:
      print(tvr.val,n)
      tvr=tvr.next
      n-=1
    return tvr

  def reverse(self):
    rev = ListNode()
    tvr= self
    while tvr:
      rev = rev.addAtBegining(tvr.val)
      tvr = tvr.next
    return rev

  def printing(self):
    tvr = self
    out = ""
    while tvr:
      out+=str(tvr.val)+"->"
      tvr=tvr.next
    print(out)

  def condiprinting(self):
    tvr = self
    out = ""
    i=0
    while tvr and i<100:
      out+=str(tvr.val)+"->"
      tvr=tvr.next
      i+=1
    print(out)



def question1(ll,ll2):
  ll.printing()
  ll = ll.reverse()
  ll.printing()
  ll2.printing()
  ll2 = ll2.reverse()
  ll2.printing()
  tvr1 = ll
  tvr = ll2
  ans = None
  while tvr1 and tvr:
    if tvr.val == tvr1.val:
      ans = tvr.val
      tvr=tvr.next
      tvr1=tvr1.next
    else:
      break
  return ans

def question2(ll):
  tvr= ll
  tvr2 = ll
  while tvr2:
    if tvr==tvr2:
      print("boom")
      return True
    tvr = tvr.next
    tvr2 = tvr2.next.next
  return False

def question3(ll,k):
  n=k
  tvr = ll
  part = ListNode()
  ans = ListNode()
  while tvr:
    if k==0:
      ans = ans.insertNode(part)
      part = ListNode()
      k=n
    part = part.addAtBegining(tvr.val)
    tvr = tvr.next
    k-=1
  part = part.reverse()
  if part.val==None:
      return ans
  ans = ans.insertNode(part)
  return(ans)

def question4(ll):
  rev = ListNode()
  rev = ll.reverse()
  rev.printing()
  tvr = ll
  tvr2 = rev
  flag =True
  while tvr:
    if tvr.val!=tvr2.val:
      flag=False
    tvr = tvr.next
    tvr2= tvr2.next
  return flag

def question5(ll):
  


ll = ListNode()
ll = ll.addAtBegining(4)
ll = ll.addAtBegining(2)
ll = ll.addAtBegining(1)
ll = ll.addAtBegining(9)
ll=ll.addAtBegining(19)
a=ll=ll.addAtBegining(21)
ll=ll.addAtBegining(32)
ll=ll.addAtBegining(34)
# ll.printing()
# print(question4(ll))
# question3(ll,3)
ll = ll.insertNode(a)
ll.condiprinting()
# question2(ll)
question5(ll)


# ll2 = ListNode()
# ll2 = ll2.addAtBegining(4)
# ll2 = ll2.addAtBegining(2)
# ll2 = ll2.addAtBegining(3)
# ll2.printing()
# n1=3
# n2=1
# print(question1(ll,ll2))