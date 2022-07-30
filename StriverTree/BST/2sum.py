# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root,direction):
        self.st = []
        self.direction = direction
        self.pushAll(root)
        

    def next(self) -> int:
        top = self.st.pop()
        if self.direction == True:
            self.pushAll(top.right)
        else:
            self.pushAll(top.left)
        return top.val
                
    def pushAll(self,root):
        tvr = root
        while tvr:    
            self.st.append(tvr)
            if self.direction==True:
                tvr = tvr.left
            else:
                tvr = tvr.right
            

    def hasNext(self) -> bool:
        if len(self.st)!=0:
            return True
        return False



class Solution:
    def findTarget(self, root, k: int) -> bool:
        if root:
            l = BSTIterator(root,True)
            r = BSTIterator(root,False)
            start = l.next()
            end = r.next()
            while start<end:
                summ = start + end
                if summ ==k:
                    return True
                elif summ<k:
                    start = l.next()
                else:
                    end = r.next()
        return None