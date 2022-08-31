class Stack:
  def __init__(self):
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




def inValid(s):
  dict = {"}":"{",")":"(","]":"["}
  lt = list(s)
  stack = Stack()
  for ele in lt:
    if ele=="{" or ele=="(" or ele=="[":
      stack.push(ele)
    if ele in dict:
      if stack.top()==-1:
        return False
      if stack.top() == dict[ele]:
        stack.pop()
      else:
        return False
  if stack.size()==0:
    return True
  return False


s = "([]){}("
print(inValid(s))

