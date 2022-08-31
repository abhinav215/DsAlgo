class MinHeap:
  def __init__(self) -> None:
    self.lt = []

  def getParent(self,index):
    return (index-1)//2

  def getLeftChild(self,index):
    return index*2+1

  def getRightChild(self,index):
    return index*2+2

  def hasParent(self,index):
    return 0 <= (index-1)//2

  def hasLeftChild(self,index):
    return len(self.lt)-1> index*2+1

  def hasRightChild(self,index):
    return len(self.lt)-1> index*2+2

  def swap(self,index1,index2):
    self.lt[index1],self.lt[index2] = self.lt[index2],self.lt[index1]

  def insert(self,data):
    self.lt.append(data)
    index = len(self.lt)-1
    self.heapup(index)

  def heapup(self,index):
    print(index,self.hasParent(index),self.lt[self.getParent(index)] > self.lt[index],self.lt[self.getParent(index)],self.lt[index])
    if self.hasParent(index) and self.lt[self.getParent(index)]>self.lt[index]:
      print(index,"lol")
      self.swap(self.getParent(index),index)
      self.heapup(self.getParent(index))

  def heapdown(self,index):
    if self.hasLeftChild(index):
      smallerChild = self.getLeftChild(index)
      if self.hasRightChild(index) and smallerChild>self.getRightChild(index):
        smallerChild=self.getRightChild(index)
      if self.lt[index]>self.lt[smallerChild]:
        self.swap(index,smallerChild)
        self.heapdown(smallerChild)

  def removeMin(self):
    data = self.lt[0]
    self.lt[0] = self.lt[-1]
    self.lt.pop()
    self.heapdown(0)
    return data


minheap = MinHeap()
minheap.insert(5)
minheap.insert(20)
minheap.insert(10)
minheap.insert(8)
minheap.removeMin()
print(minheap.lt)