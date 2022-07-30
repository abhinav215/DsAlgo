


class ListNode:
  def __init__(self, val="", next=None):
    self.val = val
    self.next = next

  def insertAtBegining(self,data):
    if self.val == "" and self.next == None:
      self.val = data
      self.next == None
      return self
    return ListNode(data,self)

  def insertAtEnd(self,data):
    tvr = self
    while tvr.next:
      print(tvr.val)
      tvr = tvr.next
    tvr.next = ListNode(data,None)
    return self

  def sizing(self):
    tvr = self
    count = 0
    while tvr:
      count+=1
      tvr = tvr.next
    return count

  def reverse(self,ll):
    trv = ll
    while trv:
      # print(trv.val)
      self = self.insertAtBegining(trv.val)
      trv = trv.next
    return self

  def printing(self):
    if self.val == "":
      print("list is blank")
      return 
    itr= self
    ans = ""
    while itr:
      # print("emer")
      ans += str(itr.val)+"-->"
      itr=itr.next
    print(ans)

  def FromMiddle(self,target):
    print(target)
    tvr = self
    while target>0:
      tvr = tvr.next
      target-=1
    print(tvr)
    return tvr

def adding(ll,ll2):
  ans = ListNode(val="",next = None)
  tvr1= ll
  tvr2 = ll2
  carry = 0
  while tvr1 or tvr2 or carry != 0:
    if not tvr1 and not tvr2:
      ans = ans.insertAtBegining(carry)
      carry = 0
    elif not tvr1:
      summ = tvr2.val+carry
      carry = summ//10
      summ = summ%10
      ans = ans.insertAtBegining(summ)
      tvr2= tvr2.next
    elif not tvr2:
      summ = tvr1.val+carry
      carry = summ//10
      summ = summ%10
      ans = ans.insertAtBegining(summ)
      tvr1 = tvr1.next
    else:
      summ = tvr1.val+tvr2.val+carry
      carry = summ//10
      summ = summ%10
      print(summ,carry)
      ans = ans.insertAtBegining(summ)
      tvr1 = tvr1.next
      tvr2= tvr2.next
  return ans  



def question1(ll):
  ll2 = ListNode()
  ans = ll2.reverse(ll)
  ans.printing()
  return (ans)

def question2(ll):
  siz = ll.sizing()
  if siz%2==0:
    target = siz//2
  else:
    target = siz//2
  ll = ll.FromMiddle(target)
  ll.printing()

def question3(ll,ll2):
  ans = ListNode()
  tvr1 = ll
  tvr2 = ll2
  while tvr1 or tvr2:
    if tvr1.val == 1000000 and tvr2.val== 1000000:
      break
    if tvr1.val <= tvr2.val :
      ans = ans.insertAtBegining(tvr1.val)
      if tvr1.next == None:
        tvr1.val=1000000
      else:
        tvr1= tvr1.next
    else:
      ans = ans.insertAtBegining(tvr2.val)
      if tvr2.next == None:
        tvr2.val=1000000
      else:
        tvr2= tvr2.next
  # ans.printing()
  ll2 = ListNode()
  ans = ll2.reverse(ans)
  ans.printing()
  return (ans)

def question4(ll,n):
  siz = ll.sizing()
  count = siz-n
  print(count)
  tvr = ll
  while tvr:
    print(count,tvr.val)
    tvr = tvr.next
    count-=1
    if count==1:
      pre = tvr
    if count ==-1:
      pre.next = tvr
      break
  ll.printing()

def question5(ll,ll2):
  ans =  adding(ll,ll2)
  final = ListNode()
  final = final.reverse(ans)
  final.printing()

def question6(ll,n):
  ll.val = ll.next.val
  ll.next = ll.next.next
  return ll


ll= ListNode()
ll = ll.insertAtBegining(9)
ll = ll.insertAtBegining(4)
ll = ll.insertAtBegining(3)
ll = ll.insertAtBegining(2)
ll = ll.insertAtBegining(1)

# ll2= ListNode()
# ll2 =ll2.insertAtBegining(1)
# ll2 =ll2.insertAtBegining(3)
# ll2 =ll2.insertAtBegining(1)

ll.printing()
# ll2.printing()
# n=2
# question4(ll,2)
# question5(ll,ll2)
n=2
ll = question6(ll.next,n)
ll.printing()
