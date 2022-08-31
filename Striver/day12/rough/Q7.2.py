
class Trie:

  def __init__(self,ch="None"):
    self.character = ch
    self.isEnd = False
    self.count = 0
    #dictionary with key as character and value as node
    self.child={}
      

  def insert(self, word: str) -> None:
    currentNode = self
    size = 32
    for i in range(size):
      if word[i] not in currentNode.child:
        currentNode.child[word[i]] = Trie(word[i])
      currentNode=currentNode.child[word[i]]
    currentNode.isEnd = True
    currentNode.count += 1

  def getMax(self,x):
    res = ""
    size=32
    xInB = '{:032b}'.format(x)
    currentNode = self
    for i in range(size):
      finding = Compliment(xInB[i])
      if finding in currentNode.child:
        res += "1"
        currentNode=currentNode.child[finding]
      else:
        res += "0"
        currentNode = currentNode.child[xInB[i]]
    # print(res)
    ans = binToDeci(res)
    return ans


def Compliment(ele):
  if ele == "1":
    return "0"
  return "1"


def binToDeci(binary_num):
  dec_num = int(binary_num, 2)
  return dec_num


def maximizeXor(nums,queries):
  trie = Trie()
  n = len(nums)
  nums.sort()
  offlineQ = []
  queryLength = len(queries)
  res = [0]*queryLength

  # for i in range(queryLength):
  #   temp = [queries[i][0],queries[i][1],i]
  #   offlineQ.append(temp)
  # offlineQ = sorted(offlineQ, key=lambda x:x[1])
  # print(offlineQ)
  for i in range(queryLength):
    queries[i].append(i)

  arrPointer =0
  for qq in range(queryLength):
    
    while arrPointer<n:
      if nums[arrPointer]<= queries[qq][1]:
        # xInB = '{:032b}'.format(nums[arrPointer])
        # trie.insert(xInB)
        trie.insert(nums[arrPointer])
        arrPointer += 1 
      else:
        break


    if arrPointer !=0:
      ans = trie.getMax(queries[qq][0])
      res[queries[qq][2]] = ans

  print(res)
  return res




    # if nums[arrPointer]<= offlineQ[i][1]:
    #   print("if",i,nums[arrPointer], offlineQ[i][1])
    #   xInB = '{:032b}'.format(nums[arrPointer])
    #   trie.insert(xInB)
    #   arrPointer+=1
    # else:    
    #   print("else")
    #   xInB = '{:032b}'.format(nums[arrPointer])
    #   ans = trie.getMax(xInB)
    #   res[offlineQ[2]] = ans
  print(res)

# offlijneQ = [xi,mi,index]

# nums = [0,1,2,3,4]
# queries = [[3,1],[1,3],[5,6]]
# nums = [5,2,4,6,6,3]
# queries=[[12,4],[8,1],[6,3]]

nums=[0,3,2,5,4]
queries=[[3,4],[5,2],[2,5],[3,1]]

maximizeXor(nums,queries)