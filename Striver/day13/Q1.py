#User function Template for python3

class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        self.arr.append(data)
        return self
    
    #Function to remove an item from top of the stack.
    def pop(self):
        if len(self.arr)==0:
            return -1
        x=self.arr.pop()
        return x
        
        