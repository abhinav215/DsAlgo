# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]

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


def nextGreaterElement(num1,arr):
  dic = {}
  n = len(arr)
  stack = Stack()
  for i in range(n-1,-1,-1):
    i=i%n
    print(i)
    while stack.top()<=arr[i]:
      stack.pop()
      if stack.size()==0:
        break
    dic[arr[i]] = stack.top()
    stack.push(arr[i])
  print(dic)
  res= []
  for ele in num1:
    res.append(dic[ele])
  print(res)





nums1 = [4,1,2]
nums2 = [1,3,4,2]
nextGreaterElement(nums1,nums2)