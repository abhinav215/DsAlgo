
class Trie:

  def __init__(self,ch="None"):
    self.character = ch
    #dictionary with key as character and value as node
    self.child={}
      
      
  def insert(self, word):
    currentNode = self
    size = 30
    for i in reversed(range(size)):
      bit = (word>>i)&1
      if bit not in currentNode.child:
        currentNode.child[bit] = Trie(bit)
      currentNode=currentNode.child[bit]

  
  def getMax(self,x):
    currentNode = self
    res = 0
    for i in reversed(range(30)):
      bit =(x>>i)&1
      if (1-bit) in currentNode.child:
        res = res | (1<<i)
        currentNode=currentNode.child[1-bit]
      else:
        currentNode=currentNode.child[bit]
    print(res)
    return res



def maximizeXor(nums,queries):
  n = len(nums)
  queryLength = len(queries)

  trie = Trie()
  res = [-1]*queryLength
  
  for i in range(queryLength):
    queries[i].append(i)

  queries = sorted( queries , key=lambda x:x[1])
  nums.sort()

  arrPointer =0
  for qq in range(queryLength):
    # print(arrPointer,n , nums[arrPointer],queries[qq][1],qq)
    while arrPointer<n and nums[arrPointer]<=queries[qq][1]:
      trie.insert(nums[arrPointer])
      arrPointer += 1 
    
    if arrPointer ==0:
      continue

    res[queries[qq][2]] = trie.getMax(queries[qq][0])

  # print(res)
  return res



# nums = [0,1,2,3,4]
# queries = [[3,1],[1,3],[5,6]]
nums = [5,2,4,6,6,3]
queries=[[12,4],[8,1],[6,3]]

# nums=[1,3,2,5,4]
# queries=[[3,4],[5,2],[2,5],[3,1]]

maximizeXor(nums,queries)