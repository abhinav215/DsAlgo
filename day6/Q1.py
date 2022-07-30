# Definition for singly-linked list.


class ListNode:
  def __init__(self, x=None,next=None):
    self.val = x
    self.next = None

def intersection(head1,head2):
  tvr1 = head1
  tvr2 = head2
  while tvr1!=tvr2:
    print(tvr1.val,tvr2.val)
    tvr1 = tvr1.next
    tvr2 = tvr2.next
    if tvr1==None and tvr2==None:
      return None
    if tvr1==None:
      tvr1=head2
    if tvr2==None:
      tvr2=head1
  # print(tvr1)
  return tvr1