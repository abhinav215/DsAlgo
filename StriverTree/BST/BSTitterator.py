class BSTIterator:
    def __init__(self, root):
        self.st = []
        while root:
            self.st.append(root)
            root = root.left
        

    def next(self) -> int:
        if len(self.st)!=0:
            top = self.st.pop() 
        else:
            top=None
        if top.right:
            tvr = top.right
            while tvr:
                self.st.append(tvr)
                tvr = tvr.left
        return top.val
                
            
    def hasNext(self) -> bool:
        if len(self.st)!=0:
            return True
        return False



