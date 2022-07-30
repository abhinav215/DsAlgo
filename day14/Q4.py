class Stack:
  def __init__(self) -> None:
    self.arr = []

  def push(self,data):
    self.arr.append(data)

  def pop(self):
    if self.sizing()==0:
      return -1
    return self.arr.pop()

  def sizing(self):
    return len(self.arr)

  def top(self):
    if self.sizing()==0:
      return -1
    return self.arr[-1]

def listmaker(data,n):
  ans = []
  for ni in range(n):
    ans.append(data)
  return ans

def rightSmaller(arr):
  stack = Stack()
  ans = listmaker(0,len(arr))
  n=len(arr)
  lastIndex= n-1
  for i in range(n-1,-1,-1):
    if stack.sizing()==0:
      ans[i] = lastIndex
      stack.push(i)
    else:
      while arr[stack.top()]>=arr[i]:
        if stack.sizing() == 0:
          break
        stack.pop()
      if stack.top() == -1:
        ans[i] = lastIndex
        stack.push(i)
      else:
        ans[i] = stack.top()-1
        stack.push(i)
  return ans
        


def leftSmaller(arr):
  stack = Stack()
  ans = []
  for i in range(len(arr)):
    # print(ans)
    # print(stack.arr,"stack")
    if stack.sizing()==0:
      ans.append(0)
      stack.push(i)
    else:
      while arr[stack.top()]>=arr[i]:
        if stack.sizing() == 0:
          break
        stack.pop()
        # print(stack.arr)
        # if stack.sizing() == 0:
        #   # print("break")
        #   break
      if stack.top() == -1:
        ans.append(0)
        stack.push(i)
      else:
        ans.append(stack.top()+1)
        stack.push(i)
  # print(ans)
  return ans

def largestRectangleArea(num):
  n = len(num)
  leftIndex = leftSmaller(num)
  rightIndex = rightSmaller(num)
  print(leftIndex)
  print(rightIndex)
  maxi = 0
  for i in range(n):
    area = num[i] *(rightIndex[i]-leftIndex[i]+1)
    print(area)
    maxi = max(maxi,area)
  print(maxi)
  return maxi





num =  [2,1,5,6,2,3,1]
largestRectangleArea(num)