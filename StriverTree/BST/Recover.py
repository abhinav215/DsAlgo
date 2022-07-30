# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        st = []
        tvr = root
        while tvr:
            st.append(tvr)
            tvr = tvr.left
        pre = -10000000
        invalid = []
        flag = 0
        while len(st)!=0:
            # print(st[0].val,st[1],len(st))
            present = st.pop()
            if flag==1:
                if present.val<pre.val:
                    invalid.append(pre)
                    invalid.append(present)
            tvr = present.right
            # print(tvr.val,"right")
            while tvr:
                st.append(tvr)
                tvr = tvr.left
            pre = present 
            flag =1
        print(len(invalid),"n")
        invalid[0].val,invalid[-1].val = invalid[-1].val, invalid[0].val
        