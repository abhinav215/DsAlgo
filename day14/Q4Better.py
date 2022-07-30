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


def largestRectangleArea(num):
  num.append(0)
  maxArea = 0
  stack=Stack()
  n = len(num)
  for i in range(n):
    print(stack.arr)
    while num[i]<num[stack.top()] and stack.size() != 0:
      index= stack.pop()
      if stack.size() == 0:
        width = i
      else:width=i-stack.top()-1
      # print(width,i,num[index])
      maxArea = max(maxArea,(num[index]*width))
    stack.push(i)
  print(maxArea)




num =  [2,1,5,6,2,3,1]
largestRectangleArea(num)