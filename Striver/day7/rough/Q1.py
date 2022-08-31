# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def sizing(self):
        count = 0
        tvr = self
        while tvr:
            count+=1
            tvr= tvr.next
        return count
        
class Solution:
    def rotateRight(self, head, k: int)  :
        tvr = ahead = head
        if tvr == None:
            return tvr
        
        
        count = 0
        tvr = head
        while tvr:
            count+=1
            tvr= tvr.next
        siz = count
        
        tvr=head
        k = k%siz
        while k !=0:
            if ahead.next == None:
                ahead= head
            else:
                ahead = ahead.next
            k-=1
        while ahead.next!=None:
            ahead = ahead.next
            tvr=tvr.next
        ahead.next=head
        nex = tvr.next
        tvr.next = None
        print(nex)
        return nex