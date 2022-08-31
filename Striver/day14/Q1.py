
class Stack:
  def __init__(self) -> None:
    self.arr=[]

  def push(self,data):
    self.arr.append(data)

  def pop(self):
    if self.size()==0:
      return -1
    return self.arr.pop()

  def top(self):
    if self.size()==0:
      return -1
    return self.arr[-1]

  def size(self):
    return len(self.arr)




def prevSmaller(self, arr):
  ans=[]
  stack = Stack()
  for ele in arr:
    while ele <= stack.top():
      stack.pop()
      if stack.size()==0:
          break
    ans.append(stack.top())
    stack.push(ele)
  return ans



