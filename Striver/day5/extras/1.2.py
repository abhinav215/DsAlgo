# Definition for singly-linked list.


class ListNode:
    def __init__(self, val="", next=None):
        self.val = val
        self.next = next

    def reverse(self,ll):
        trv = ll
        while trv:
            print(trv.val)
            self = self.AddAtBegining(trv.val)
            trv = trv.next
        return self
    
    def AddAtBegining(self,data):
        if self.val == "" and self.next == None:
            self.val = data
            self.next == None
            return self
        return ListNode(data,self)


# def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
def reverseList(self, head):
  ll2 = ListNode()
  ans = ll2.reverse(head)
  print(ans.next)
  return (ans)